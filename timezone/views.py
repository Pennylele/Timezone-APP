from django.shortcuts import render
from django.http import HttpResponse
import datetime, pytz
from .forms import DateTimeForm
import re
from django.contrib import messages


def home(request):
	args = {}
	fmt = '%Y-%m-%d %H:%M'
	args['tzs'] = pytz.all_timezones

	if request.method == "POST":
		form = DateTimeForm(request.POST)
		args['form'] = form
		if form.is_valid():
			datetime_form = form.save()
			user_tz = form.cleaned_data.get('User_Time_Zone')
			user_dt = form.cleaned_data.get('User_Date_Time')
			user_timezone = pytz.timezone(user_tz)
			dt_lst_raw = re.split(r'[-\s:]', user_dt)
			dt_lst_int = [int(i) for i in dt_lst_raw]
			try:
				user_dt_update = datetime.datetime(*dt_lst_int[:])
				user_dt_tzaware = user_timezone.localize(user_dt_update)

				if request.POST.get("tz"):
					selected_tz = request.POST.get("tz")
				else:
					selected_tz = 'UTC'

				converted_user_time = user_dt_tzaware.astimezone(pytz.timezone(selected_tz))
				args['converted_user_time'] = converted_user_time.strftime(fmt)
				args['selected_tz'] = selected_tz
				args['conv_time'] = converted_user_time.strftime(fmt)
				args['user_dt'] = user_dt
				args['user_tz'] = user_tz

			except ValueError:
				messages.error(request, 'The date time format filled in previously was not correct. \nPlease follow the format (YYYY-MM-DD HH:MM)')

			# user_dt_tzaware = user_dt.replace(tzinfo=user_timezone)
			# user_dt_tzaware_adjust = user_dt_tzaware - datetime.timedelta(minutes=53)
			# Had to revert back 53min as the tz awareness seems to fast forward 53min.
			# Had to abandon the above, because the time conversion always have errors. Could be a bug.


	else:
		form = DateTimeForm()
		args['form'] = form
	return render(request, 'timezone/home.html', args)
	

def timer(request):
	return HttpResponse('<h1>Timer</h1>')
