.PHONY: tags

tags:
	find gizela -name "*.py" | xargs ./ptags.py
clean:
	rm -f tags
