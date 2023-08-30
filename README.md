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

// Generate a base64 encoded JWT assertion
var jwtHeader = { "alg": "RS256", "typ": "JWT" };
var encodedHeader = Buffer.from(JSON.stringify(jwtHeader)).toString('base64');
var encodedPayload = Buffer.from(JSON.stringify(jwtPayload)).toString('base64');
var assertion = encodedHeader + "." + encodedPayload;

// Sign the assertion with the private key
var privateKey = serviceAccountJson.private_key;
var signature = crypto.createSign('RSA-SHA256').update(assertion).sign(privateKey, 'base64');

var signedAssertion = assertion + "." + signature;

// Send a request to the token endpoint to exchange the signed JWT assertion for an access token
httpClient.send('POST', serviceAccountJson.token_uri, null, 'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion=' + signedAssertion, function(response) {
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









#Token Pooling
Simple Microservice for serving tokens.

## Installation

Setup virtual environment
```bash
sudo apt-get install -y python3-pip

sudo apt install python3-venv -y  && python3 -m venv venv && . venv/bin/activate

```

Install requirments

```
sudo pip3 install -r requirements.txt
```

Setup Cache
```
sudo apt-get install memcached

memcached -u root &

```
Run application

```
python main.py

```

API details

```
/post_token

Description:
    Create a token in Database.
params:
    token_name
--------------------------------
/get_token

Description:
    Get a token from the Microservice.
params:
    None
--------------------------------
/get_token_status

Description:
    Get usage status of all tokens.
params:
    None

```
