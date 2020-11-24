run :
	uvicorn app.main:app --reload

clean :
	find . | grep -E "(__pycache__)" | xargs rm -rf