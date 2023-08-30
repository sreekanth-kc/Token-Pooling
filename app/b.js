// Extract the service account JSON from a Key/Value Map or directly set it here
var serviceAccountJson = {
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "your-private-key-id",
  "private_key": "your-private-key",
  "client_email": "your-client-email",
  "client_id": "your-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-client-email"
};

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

var jwtHeader = { "alg": "RS256", "typ": "JWT" };

// Encode payload and header
var encodedPayload = btoa(JSON.stringify(jwtPayload));
var encodedHeader = btoa(JSON.stringify(jwtHeader));

// Combine header and payload
var assertion = encodedHeader + "." + encodedPayload;

// Sign the assertion with the private key
var privateKey = serviceAccountJson.private_key;

// Here you would need to implement RSA-SHA256 signing manually since there is no built-in method for it in Apigee's scripting environment

// Send a request to the token endpoint to exchange the signed JWT assertion for an access token
httpClient.send('POST', serviceAccountJson.token_uri, null, 'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion=' + assertion, function(response) {
  if (response.status === 200) {
    var responseBody = JSON.parse(response.responseText);
    var accessToken = responseBody.access_token;

    // Here you can use the accessToken for your API requests
    // Example: httpClient.send() or http.request()

    // Send the access token back in the response (for demonstration purposes)
    context.setVariable("gcp_access_token", accessToken);
  } else {
    // Handle error
    console.error("Error getting access token:", response.status, response.reasonPhrase);
  }
});
