from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView

from skills.models import Skill
from examinations.models import Exercice, Test

from .utils import user_is_professor

urlpatterns = patterns('promotions.views',
    url(r'^dashboard/$', 'dashboard', name='professor_dashboard'),

    url(r'^lesson/(?P<pk>\d+)/$', 'lesson_detail_view', name='professor_lesson_detail_view'),
    url(r'^lesson/(?P<lesson_pk>\d+)/skill/(?P<skill_code>\w+)/$', 'lesson_skill_detail_view', name='professor_lesson_skill_detail_view'),

    url(r'^student/(?P<pk>\d+)/$', 'student_detail_view', name='professor_student_detail_view'),
    url(r'^student/(?P<pk>\d+)/test/(?P<test_pk>\d+?)/$', 'student_test_view', name='professor_student_test_view'),

    url(r'^regenerate_student_password/$', 'regenerate_student_password', name='professor_regenerate_student_password'),

    url(r'^skill/(?P<slug>\w+)/$', user_is_professor(DetailView.as_view(model=Skill, slug_field="code", template_name="professor/skill_detail.haml")), name='professor_skill_detail_view'),
    url(r'^pedagogical/(?P<slug>\w+)/$', 'edit_pedagogical_ressources', name='professor_skill_edit_pedagogical_ressources'),
    url(r'^skill_tree/$', user_is_professor(ListView.as_view(model=Skill, template_name="professor/skill_tree.haml")), name='professor_skill_tree'),

    url(r'^validate_skill/(?P<student_skill>\d+)/$', 'validate_student_skill', name='professor_validate_student_skill'),
    url(r'^unvalidate_skill/(?P<student_skill>\d+)/$', 'unvalidate_student_skill', name='professor_unvalidate_student_skill'),
    url(r'^default_skill/(?P<student_skill>\d+)/$', 'default_student_skill', name='professor_default_student_skill'),

    url(r'^lesson_tests_and_skills/(?P<lesson_id>\d+).json$', 'lesson_tests_and_skills', name='lesson_tests_and_skills'),
    url(r'^add_test_for_lesson/$', 'add_test_for_lesson', name='add_test_for_lesson'),

    url(r'^exercices/$', 'exercice_list', name='professor_exercice_list'),
    url(r'^exercices/(?P<pk>\d+)/$', user_is_professor(DetailView.as_view(model=Exercice, template_name="professor/exercice_detail.haml")), name='professor_exercice_detail'),

    # TODO: professor can only see his tests
    url(r'^test/(?P<pk>\d+)/$', user_is_professor(DetailView.as_view(model=Test, template_name="professor/test_detail.haml")), name='professor_test_detail'),

    url(r'^lesson/(?P<pk>\d+)/students_password_page/$', 'students_password_page', name='professor_students_password_page'),
)
