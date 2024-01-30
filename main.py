import random
import requests

url = 'https://leetcode.com/graphql/'

headers = {
    'authority': 'leetcode.com',
    'content-type': 'application/json',
}

tag_weights = {
    "depth-first-search": {"difficulty": "Medium", "ROI": "High"},
    "breadth-first-search": {"difficulty": "Low", "ROI": "High"},
    "two-pointers": {"difficulty": "Medium", "ROI": "High"},
    "linked-list": {"difficulty": "Low", "ROI": "High"},
    "stack": {"difficulty": "Medium", "ROI": "Medium"},
    "queue": {"difficulty": "Medium", "ROI": "Medium"},
    "heap-priority-queue": {"difficulty": "Medium", "ROI": "Medium"},
    "greedy": {"difficulty": "High", "ROI": "Low"},
    "dynamic-programming": {"difficulty": "High", "ROI": "Low"},
    "trie": {"difficulty": "Medium", "ROI": "Medium"},
    "union-find": {"difficulty": "Medium", "ROI": "Low"},
}

# Calculate weights based on difficulty and ROI
total_weight = sum(1 / (1 + (tag_weights[tag]["difficulty"] == "High") + (tag_weights[tag]["difficulty"] == "Medium") + (tag_weights[tag]["ROI"] == "Low")) for tag in tag_weights)

# Create the weighted dictionary
weighted_dict = {tag: 1 / (1 + (tag_weights[tag]["difficulty"] == "High") + (tag_weights[tag]["difficulty"] == "Medium") + (tag_weights[tag]["ROI"] == "Low")) / total_weight for tag in tag_weights}

# Print the result
print(weighted_dict)

tag = random.choices(list(weighted_dict.keys()), weights=list(weighted_dict.values()))[0]

data = {
    'query': '''
        query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
            problemsetQuestionList: questionList(
                categorySlug: $categorySlug
                limit: $limit
                skip: $skip
                filters: $filters
            ) {
                total: totalNum
                questions: data {
                    acRate
                    difficulty
                    freqBar
                    frontendQuestionId: questionFrontendId
                    isFavor
                    paidOnly: isPaidOnly
                    status
                    title
                    titleSlug
                    topicTags {
                        name
                        id
                        slug
                    }
                    hasSolution
                    hasVideoSolution
                }
            }
        }
    ''',
    'variables': {
        'categorySlug': 'all-code-essentials',
        'skip': 0,
        'limit': 50,
        'filters': {'difficulty': 'MEDIUM', 'tags': [tag], 'listId': 'wpwgkgt'},
    },
    'operationName': 'problemsetQuestionList',
}

response = requests.post(url, headers=headers, json=data)
questions = response.json()['data']['problemsetQuestionList']['questions']
q = random.choice(questions)
print(f"Question: {q['frontendQuestionId']}. {q['title']}")
