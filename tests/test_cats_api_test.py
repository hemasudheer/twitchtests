import requests

cats_home_paege_url = "https://catfact.ninja"


def test_fetch_random_cat_fact():
    """ Test to fetch a random cat fact"""
    response = requests.get(f"{cats_home_paege_url}/fact")
    # Verify the response status code
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Validate the response structure
    json_data = response.json()
    assert "fact" in json_data, "The 'fact' field is missing in the response."
    assert isinstance(json_data["fact"], str) and len(json_data["fact"]) > 0, "The 'fact' field is not a valid non-empty string."


def test_fetch_list_of_cat_facts():
    """Test to fetch a list of cat facts with a specified limit"""
    limit = 3
    response = requests.get(f"{cats_home_paege_url}/facts", params={"limit": limit})

    # Verify the response status code
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Validate the response structure
    json_data = response.json()
    assert "data" in json_data, "The 'data' field is missing in the response."
    assert isinstance(json_data["data"], list), "The 'data' field is not a list."
    assert len(json_data["data"]) == limit, f"Expected {limit} facts, but got {len(json_data['data'])}."

    # Validate each fact in the response
    for fact in json_data["data"]:
        assert "fact" in fact, "A 'fact' field is missing in one of the data elements."
        assert isinstance(fact["fact"], str) and len(fact["fact"]) > 0, "The 'fact' field is not a valid non-empty string."


def test_all_breeds_of_cats():
    """ Test to fetch all breeds of cats"""
    response = requests.get(f"{cats_home_paege_url}/breeds")
    # Verify the response status code
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


def test_limit_cat_breeds():
    """Test to fetch cat breeds with a specified limit"""
    limit = 5
    response = requests.get(f"{cats_home_paege_url}/breeds", params={"limit": limit})

    # Verify the response status code
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Validate the response structure
    json_data = response.json()
    assert "data" in json_data, "The 'data' field is missing in the response."
    assert isinstance(json_data["data"], list), "The 'data' field is not a list."
    assert len(json_data["data"]) == limit, f"Expected {limit} facts, but got {len(json_data['data'])}."

