// Extract the service account JSON from a Key/Value Map
var serviceAccountJson = JSON.parse(context.getVariable("serviceAccountMap.service_account_json"));

// Construct the JWT assertion
var currentTime = Math.floor(Date.now() / 1000);
var expirationTime = currentTime + 3600; // Token valid for 1 hour

var jwtPayload = {
  "iss": serviceAccountJson.client_email,
  "scope": "https://www.googleapis.com/auth/cloud-platform",
  "aud": serviceAccountJson.token_uri,
  "exp": expirationTime,
  "iat": currentTime
};

// ... (rest of the JWT payload construction as mentioned in previous responses)

// Send a request to the token endpoint to exchange the signed JWT assertion for an access token
httpClient.send('POST', serviceAccountJson.token_uri, null, 'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion=' + assertion, function(response) {
  if (response.status === 200) {
    var responseBody = JSON.parse(response.responseText);
    var accessToken = responseBody.access_token;

    // Log the access token for debugging purposes
    console.log("Generated GCP Access Token:", accessToken);

    // Use the accessToken for your API requests
    // Example: httpClient.send() or http.request()

    // Send the access token back in the response (for demonstration purposes)
    context.setVariable("gcp_access_token", accessToken);
  } else {
    // Handle error
    console.error("Error getting access token:", response.status, response.reasonPhrase);
  }
});
