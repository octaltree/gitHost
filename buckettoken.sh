#!/bin/bash

bucketkey="Ev4c4krDQqHyRd2XH6"
bucketsecret="TvvCNhsZGwFWJ6eBM9Q2crLDUawsQ4Ar"
bucketcode="FPHfbzscQt5NkAFWvp"


curl -X POST -u "$bucketkey:$bucketsecret" \
  https://bitbucket.org/site/oauth2/access_token \
  -d grant_type=authorization_code\
  -d code=$bucketcode > tmp
