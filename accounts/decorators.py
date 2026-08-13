from django.contrib.auth.decorators import user_passes_test


def soignant_required(view_func):
    return user_passes_test(lambda u: u.is_authenticated and u.is_soignant())(view_func)


def patient_required(view_func):
    return user_passes_test(lambda u: u.is_authenticated and u.is_patient())(view_func)


def centre_required(view_func):
    return user_passes_test(lambda u: u.is_authenticated and u.is_centre())(view_func)