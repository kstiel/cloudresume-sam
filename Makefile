.PHONY: build

build:
	sam build

deploy-infra:
	sam build && sam deploy

deploy-site:
	aws s3 sync ../resume_site s3://kaungsithu-website