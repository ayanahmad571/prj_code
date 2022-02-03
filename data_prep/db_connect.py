import os
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="prj"
)

# Create Table
# CREATE TABLE `prj`.`data_lab` ( `id` INT(25) NOT NULL AUTO_INCREMENT , `uid` INT(100) NOT NULL , `bot` INT(100) NULL , `num_likes_per_num_friends` INT(100) NULL , `follow_friends_ratio` INT(100) NULL , `max_time_bw_retweets` INT(100) NULL , `re_per_tweet` INT(100) NULL , `num_likes` INT(100) NULL , `num_likes_per_follower` INT(100) NULL , `age_account` INT(100) NULL , `num_tweets` INT(100) NULL , `location` INT(100) NULL , `len_username` INT(100) NULL , `has_photo` INT(100) NULL , `likes_per_day` INT(100) NULL , PRIMARY KEY (`id`(25))) ENGINE = MyISAM;

#ALTER TABLE `data_lab` ADD `id` INT(25) NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY (`id`);

myscursor = mydb.cursor()
# mycursor.execute("SELECT * FROM ms_views limit 100")
# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

