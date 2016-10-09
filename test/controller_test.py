import controller

def test_time_to_str():
	assert controller.time_to_str(0) == "00"
	assert controller.time_to_str(10) == "10"
	assert controller.time_to_str(2) == "02"

def test_translate_to_time():
	assert controller.translate_to_time(10) == "00:00:10"
	assert controller.translate_to_time(60) == "00:01:00"
	assert controller.translate_to_time(3600) == "01:00:00"
	assert controller.translate_to_time(3700) == "01:01:40"

def test_translate_from_time():
	assert controller.translate_from_time("00:00:10") == 10
	assert controller.translate_from_time("00:01:00") == 60
	assert controller.translate_from_time("01:00:00") == 3600
	assert controller.translate_from_time("01:01:40") == 3700