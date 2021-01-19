# yaml -> md -> html

docs/%index.md: docs/%index.yaml
	$(RENDRE) -d $@ tmpl-0006 > $<

pre_build:
	make docs/*/index.yaml

serve:
	make pre_build
	elstir serve

