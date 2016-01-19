#!/bin/bash


bucketkey="Ev4c4krDQqHyRd2XH6"
bucketsecret="TvvCNhsZGwFWJ6eBM9Q2crLDUawsQ4Ar"
refreshtoken="2g7VCmzNcR8p3XDWa6"

curl --verbose -X POST -u "$bucketkey:$bucketsecret"\
  https://bitbucket.org/site/oauth2/access_token\
  -d grant_type=refresh_token\
  -d refresh_token=$refreshtoken >  tmp
