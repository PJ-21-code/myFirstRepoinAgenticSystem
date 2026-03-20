1. What is the role of query parameters in this request
   The role of query parameters is to select repositories on the basis of word(e.g. we want python repositories), sorting done on the basis of no of stars in a descending order where there will contain only 5 repo on each page.
   Basically, it is used to segregate repositories on the basis of some parameters so that we can fetch them using requests library.

2. Why do we use response.json() instead of response.text?
   response.text function gives plain text(string) as it is present in the link while response.json() converts python object into dictionary so that we can use keys present in our api link to fetch repository items conviniently.   