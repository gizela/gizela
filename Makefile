actual=gizela/data/NetworkAdj.py
actual=gizela/data/POINT_LOCAL_STATUS.py
actual=gizela/data/PointBase.py
actual=gizela/data/PointLocal.py
actual=gizela/data/PointList.py

.PHONY: tags

actual:
	python3 $(actual)

tags:
	find gizela -name "*.py" | xargs python ptags.py

clean:
	rm -f tags

