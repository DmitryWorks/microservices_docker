# microservice testing script

from recommendations import RecommendationService
from recommendations_pb2 import BookCategory, RecommendationRequest

def test_recommendations():
	service = RecommendationService()
	request = RecommendationRequest(
		user_id = 1,
		category = BookCategory.MYSTERY,
		max_result = 1
	)

	response = service.Recommend(request, None)
	
	assert len(response.recommendations) == 1

testing = test_recommendations()
print(testing)