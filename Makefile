export PYTHONPATH=/home/kubin/git/gizela
actual=gizela/data/NetworkAdj.py
actual=gizela/adj/local/PointBase.py
actual=gizela/adj/local/POINT_LOCAL_STATUS.py
actual=gizela/adj/local/PointLocal.py
actual=gizela/adj/local/PointList.py

.PHONY: tags

actual:
	echo $(PYTHONPATH)
	python3 $(actual)

tags:
	find gizela -name "*.py" | xargs python ptags.py

clean:
	rm -f tags

