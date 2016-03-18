from django.conf.urls import url, include

from exercise import views

exercise_list_urls = [
    url(r'^(?P<filter_type>\w+)/(?P<filter_main>\w+)/$', views.list_exercises, name='list_exercises'),
    url(r'^(?P<filter_type>\w+)/(?P<filter_main>\w+)/(?P<second_filter>\w+)/$',
        views.list_exercises, name='list_exercises'),
]


urlpatterns = [
    url(r'^$', views.exercise_home, name='exercise_home'),
    url(r'^my_workouts/$', views.my_workouts, name='my_workouts'),
    url(r'^workout/(?P<pk>[0-9]+)/', views.workout_detail, name='workout_detail'),
    url(r'^create_workout/$', views.create_workout, name='create_workout'),
    url(r'^record_workout/$', views.record_workout, name='choose_workout_to_log'),
    url(r'^record_workout/(?P<pk>[0-9]+)/', views.record_workout, name='record_workout'),
    url(r'^search/workout/$', views.search_workout, name='workout_search'),
    url(r'^add_to_workout/(?P<pk>[0-9]+)/', views.add_to_workout, name='add_to_workout'),
    url(r'^move_up/(?P<pk>[0-9]+)/', views.move_exercise_up, name='move_up'),
    url(r'^link/(?P<pk>[0-9]+)/', views.link, name='link'),
    url(r'^unlink/(?P<pk>[0-9]+)/', views.unlink, name='unlink'),
    url(r'^remove_from_workout/(?P<pk>[0-9]+)/', views.remove_from_workout, name='remove_from_workout'),

    url(r'^list/', include(exercise_list_urls)),
    url(r'^search/exercise/', views.search_exercises, name='exercise_search'),
    url(r'^exercise/(?P<pk>[0-9]+)/', views.exercise_detail, name='exercise_detail'),
    url(r'^create_exercise/$', views.create_exercise, name='create_exercise'),

    url(r'^workout_logs/$', views.log_list, name='workout_logs'),
    url(r'^workout_logs/(?P<pk>[0-9]+)/', views.log_detail, name='workout_log_detail'),

    url(r'^routines/my/$', views.my_routines, name='my_routines'),
    url(r'^routines/followed/$', views.followed_routines, name='followed_routines'),
    url(r'^routines/(?P<pk>[0-9]+)/', views.routine_detail, name='routine_detail'),
    url(r'^routines/search/', views.search_routines, name='routine_search'),
    url(r'^routines/create/', views.create_routine, name='create_routine'),
    url(r'^routines/follow/(?P<pk>[0-9]+)/', views.follow_routine, name='routine_follow'),
    url(r'^routines/unfollow/(?P<pk>[0-9]+)/', views.unfollow_routine, name='routine_unfollow'),

]
