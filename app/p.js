var privateKey = "your_actual_private_key_here"; // Retrieve the private key value from wherever you store it

// Store the private key in a KVM entry
var kvmMap = KeyValueMap("your_kvm_name");
kvmMap.set("myPrivateKey", privateKey);

========

<JWT name="JWT-Generate">
  <Algorithm>RS256</Algorithm>
  <PrivateKey>
    <KVM>
      <MapIdentifier>your_kvm_name</MapIdentifier>
      <EntryIdentifier>myPrivateKey</EntryIdentifier>
    </KVM>
  </PrivateKey>
  <Claims>
    <Claim name="iss" value="{your-client-email}" />
    <Claim name="aud" value="{your-audience}" />
  </Claims>
</JWT>
