## 0. Introduction

Registration or Authentication is not implemented ATM.

## 1. How They Made

The backend appears to be constructed by Privy except SMS verification.  
Maybe we will be Arkham'd up.

## 2. Vulnerabilities

1. The implementation of rate limits in SMS authentication is inadequate, allowing for possible bypasses.
2. Invite codes can be redeemed an unlimited number of times without any restrictions, leading to depletion.
3. All user information can be accessed. (Actually, it's the ~~worst~~ specification but it's more convenient to explain it like this for the next explanation.)
4. Information regarding the senders of messages to a group can be retrieved in real time due to a lack of authentication.
5. The paths of images uploaded by users can be predicted by chaining the aforementioned vulnerabilities.
   - Vuln #3, gather user names and addresses.
   - Vuln #4, wait for a user to send a message to the group.
     - Check the user's address from the user name.
     - Check the current time.
       - The path comprises the user's address and the Unix Timestamp in milliseconds.

## 3. Problem

You can check the newly registered users to buy tokens ASAP, so basically, this platform is now almost f\*\*\*ed by a bot.

## 4. Fun Facts

1. You don't have to deposit for debugging since all validation is client-side.
2. All endpoint is from kosetto.com which is a dead NFT project.
3. 08/20/2023 (JTC). All Japanese international phone numbers are temporarily blacklisted because of me.
4. Now [all public users information is exposed](https://gist.github.com/banteg/76d141fea2e658e5d2854944342f2d3d) by [banteg](https://twitter.com/bantg/status/1693547023977382277)

## 5. My Opinions

https://twitter.com/lutwidse_miceon/status/1693338817095483729
