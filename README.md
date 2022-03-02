# prj_code

### Pre-Requisite
Must have a specific file structure. Will be specified later

### AIM
Will be using the TwiBot data and the Swedish Election features to identify bot accounts in the presidential dataset.

### List of features:
There are various features that we wont be able to use since we are unable to fetch data about them.
 - \# given likes per \# friends 
 - Followers-friends ratio 
 - Maximum time between retweets 
 - \# retweets achieved per tweet 
 - Standard deviation of time between retweets 
 - Median time between retweets 
 - Population standard deviation of time between retweets 
 - Mean time between retweets 
 - \# given likes 
 - \# given likes per \# followers
 - \# urls per tweet

#### New Features - user metadata
- statuses_count                count
- followers_count               count
- friends_count                 count
- favourite_count               count
- listed_count                  count
- default_profile_binary        binary
- profile_use_background_image  binary
- verified                      binary

#### New Features - derived features

- tweet_freq                    real-valued
- followers_growth_rate         real-valued
- friends_growth_rate           real-valued
- favourites_growth_rate        real-valued
- listed_growth_rate            real-valued
- followers_friends_ratio       real-valued
- screen_name_length            count 
- num_digits_in_screen_name     count
- name_length                   count
- num_digits_in_name            count
- description_length            count
- screen_name_likelihood        real-valued

#### File Structure

- data_fetch, data_fet_twi_bot, data_fetch_cresci will  collect data from respective data sets in the defined directory and will extract features from them
- as