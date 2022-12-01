# helper function to run features


def detect_user(user):
    if user.role == 1:
        redirectUrl  = 'vendorDashboard'
        return redirectUrl
    elif user.role == 2:
        redirectUrl  = 'custDashboard'
        return redirectUrl
    elif user.role == None and user.is_superadmin:
        redirectUrl = '/admin'
        return redirectUrl