export PYTHONPATH=/home/kubin/git/gizela
actual=gizela/adj/local/PointBase.py
actual=gizela/adj/local/POINT_LOCAL_STATUS.py
actual=gizela/adj/local/PointLocal.py
actual=gizela/adj/local/PointList.py
actual=gizela/adj/local/PointLocalCovMat.py
actual=gizela/adj/local/PointListCovMat.py
actual=gizela/adj/local/PointListEpoch.py
actual=gizela/adj/geodetic/PointGeodetic.py
actual=gizela/util/Ellipsoid.py
actual=gizela/adj/local/NetworkAdj.py

.PHONY: tags

actual:
	echo $(PYTHONPATH)
	python3 $(actual)

tags:
	find gizela -name "*.py" | xargs python ptags.py

clean:
	rm -f tags

