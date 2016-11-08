win32: make_any_time
	../../tools/Build.py laserPrinter.spec.win32
	touch make_any_time
cygwin: make_any_time
	../../tools/Build.py laserPrinter.spec.cygwin
	touch make_any_time
linux: make_any_time
	../../tools/Build.py laserPrinter.spec.linux
	touch make_any_time
clean:
	rm -rf build dist

src_clean:
	find . -name "*.pyc"|xargs rm -rf
	find . -name "*~"|xargs rm -rf

