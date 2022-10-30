from car_collection_app.car_collection_web.models import Profile, Car


def get_profile():
    profile = Profile.objects.first()
    if profile:
        profile.cars = Car.objects.all()
        profile.cars_count = profile.cars.count()
        if profile.first_name and profile.last_name:
            profile.full_name = f"{profile.first_name} {profile.last_name}"
        elif profile.first_name and not profile.last_name:
            profile.full_name = f"{profile.first_name}"
        elif profile.last_name and not profile.first_name:
            profile.full_name = f"{profile.last_name}"
        if profile.cars:
            profile.cars_sum = sum(c.price for c in profile.cars)
    return profile
