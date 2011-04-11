proj=vod-zen-xyz vod-zen-z sikma-zen-xyz sikma-zen-z\
     sikma-zen-smer-xyz sikma-zen-smer-z\
     vod-zen-smer-xyz vod-zen-smer-z\
     vod-vec sikma-vec\
     sikma-vec-zen\
     vod-zen-dh-xyz\
     vod-zen-coord-xyz


all:
	make $(proj:=.txt)

%.txt: %.xml
	./gama-local $< --text $@ --obs $(@:.txt=.obs) --latitude 45 --ellipsoid bessel

clean:
	rm -f $(proj:=.txt)
	rm -f $(proj:=.obs)
