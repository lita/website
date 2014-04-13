Title: Databases
Date: 2014-03-23
Slug: databases
Tags: databases, web, hacker school

I've been learning a lot about databases lately, and what sort of databases are out there currently. A fellow Hacker Schooler pointed me [A Dozen Databases in 45 Minutes][dataTalk] by Eric Redmond, which was a pretty good overview of whats out there.

After listening to this presentation and talking with another Hacker Schooler about databases, I thought I'd share what I learned. I am mostly going to go deeper with Open Source databases, so anyone can try using them at home.

## Type: Relational Databases  
#### Examples: MySQL, PostgreSQL  
This is the most common database out there. It has been around for a long time and it is very mature. You have a collection of 2D tables (rows and columns), very similar to Excel spreadsheets. However, you can add relationships between tables. Lets say you have the following two tables.

<table style="width:400px">
<tr>
  <th>name</th>
  <th>postal_code</th>     
  <th>country_code</th>
</tr>
<tr style="border-top: 1px solid black">
  <td>San Francisco</td>
  <td>94109</td>        
  <td>us</td>
</tr>
<tr>
  <td>Portland</td>
  <td>97205</td>      
  <td>us</td>
</tr>
</table>

<table style="width:300px">
<tr>
  <th>country_code</th>
  <th>country_name</th>     
</tr>
<tr style="border-top: 1px solid black">
  <td>us</td>
  <td>United States</td>        
</tr>
<tr>
  <td>mx</td>
  <td>Mexcio</td>
</tr>
<tr>
  <td>au</td>
  <td>Australia</td>
</tr>
</table>

You can create a relationship between the two tables through the "country_code" attribute, which they both share. I prefer to think of these relational attributes as pointers to different tables. Probably because of my C++ background...

![Table Example](/images/table.png)
<p class=subnote> Note: Image taken from <u>Seven Databases in Seven Weeks</u> by Eric Redmond and Jim R. Wilson </p>

You have to define a <b>schema</b> when you create your table, which declares what types of objects your database is going to store for that table. It's like defining your types in a static-type programming language. This can be annoying, since you have to architect your data ahead of time. Sometimes you don't know what kind of data you will want to store or how to query it ahead of time. Data normalization is a hard problem, which is removing duplicated data and finding which values are the right keys.

<table>
    <tr>
        <td>
        <img src='/images/schema.png'>
        </td>
    </tr>
    <tr>
        <td>
            <center>Schema</center>
        </td>
    </tr>
    <tr>
        <td>
        <img src='/images/schema_table.png'>
        </td>
    </tr>
     <tr>
        <td>
            <center>Table</center>
        </td>
    </tr>
</table>
 
Because of the schema, relational databases are strict with what kind of data you put in them. If you define the type of 'dob' to be a "date", it has to take a particular format, MM/DD/YYYY. If you try to input a string or random numbers, the database will throw an error.

What's nice and powerful about a relational-database are the queries you can make. You can use SQL to filter out data you care about by doing JOINS and getting a new table. This blog post has a great explanation of JOINS if anyone is interested in reading further.

[A Visual Explanation of SQL Joins](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/)

The downsides are that relational databases are pretty inflexible. Because you have to define a schema ahead of time, you can't change what your database is going to store on the fly. However, you are guaranteed that the data will be what the schema says it will be, so you don't have to worry about validation. 

If you design your schema poorly, your database queries can get expensive. If you are doing a lot of joins to calculate your result, queries will take a long time. I can see as your website grows, it would be a lot of work to refactor your schema as your needs change.

Another major downside of relational databases is scaling. You can improve the hardware of your server, which is expensive and may cause downtime. But this has a ceiling as well. You can try distributive computing, by breaking up your database into clusters (multiple computers). But splitting up your database is not that easy..

A lot of relational-databases do **sharding** to scale to multiple servers, which is a fancy term for splitting up the rows of the table in some logical way to different servers. 

<img src="/images/sharding.jpg" alt="Sharding" style="width: 400px;"/>
<p class=subnote> Crude, but awesome, example of sharding! Imagine this table has only one column and holds rows 'eggs, other crap, dogs, and fish'. Now dogs and fish are split out to they own separate servers, while egg and crap are within their own servers.
<p class=subnote> Note: Image taking from Shai Wininger from his <a href="http://hackingshmacking.com/tag/haproxy/">blog entry</a>.

However, figuring out how to split up your data in a relational database is not trivial. You will need to write sharding code, also known as a load balancer, that manages where your data and queries go. Handing JOIN, and UNION also gets super complicated, since you have to deal with which computers to look at, not just tables. Overall, it is a lot of work to scale a relational database.

There are systems that do auto-sharding, like MySQL Cluster. But overall, relational databases get non-linear pretty quickly, causing latency issues, especially if your schema sucks. You can scale your relational database with big data, but it is a lot of work and/or a lot of money. Overall, there are better solutions out there if you know your database is going to grow massively. 

## Type: Key-Value Store  
#### Examples: Riak, HBase, Redis, memcached
Databases with the key-value model store data based on a key, which is VERY similar to a hash table. Because of the simplicity of their design, partitioning (horizontal scaling) is done really easily. Just split the data based on the hash function. 

###Redis and memcached
However, with memcached and Redis, all the data lives in RAM. Because of this, both databases are incredibly fast at reads and writes. This is great if you are working with time sensitive data, like stock prices. Redis can write to disk if it ever shuts down, so it stays persistence, but can't read from disk while its on. Memcached doesn't do this, so the data is lost when it shuts down. 

Redis is currently working on [clustering in order to make it scalable][rcluster], but it is in its alpha stages. Overall, I wouldn't use these databases as your main data store unless you are working on something small. Rather I would complement your web app with another database, like Riak, HBase or another relational/document database.

Speaking of Riak and HBase, lets get into these key-value stores!

###Riak
Riak is based on the Amazon Dynamo paper, which is apparently a famous paper according to Lindsey Kuper! It's a fairly new database, and it seems to be what all the cool kids are talking about nowadays. Riak and HBase are both meant to be used for distributed systems. They were designed with scaling in mind and thus are easily able to be partitioned out to different servers.

What's cool about Riak is that any sever in your distributed system can read or write to the database! It is also fault-tolerant, which means you won't lose data if few of your servers die. But there is a trade-off. You can't get immediate consistency. This is because while you are writing to one server, it will take awhile to update your other servers about it. However, they do guarantee **eventual consistency**. This basically means that if no one writes to the database for awhile, the database will eventually be consistent. Sounds kind of shady to me. However, this database is great if you need to be able to read and write quickly while giving up a little bit of consistency. 

Riak also has this awesome documentation where they annotate the Amazon Dynamo paper with how Riak was designed. If you are interested in learning the internals of Riak and how it is implemented, I highly recommend reading this!

[Dynamo: Amazon's Highly Available Key-Value Store with Riak annotations](http://docs.basho.com/riak/latest/theory/dynamo/)

In Riak, you can query for data by giving it a key. You can also assign a secondary index during write-time, which is like giving the object a second key. So you can access the object by querying either key. You can even do a full on text-search to find your data!

During this portion of the talk, I also learned how <b>MapReduce</b> worked! This is how Riak implements the full-text search. I always thought of MapReduce as this fancy buzzword, but after Eric explained it, I felt silly not knowing about it sooner. I'd thought I share it with you all!

Lets say you have a partitioned key-value store in four servers. In this key-value, we store a username and age. We want to calculate the average age of all the users we have for our website. One way to go about it is to query four servers for all the users and manually calculate the average age on the client machine. But that would be REALLY slow. However, with MapReduce, each server calculates the average age within their database and pushes that result upstream! We map the function to the servers, in which the servers run that function on each of their data-entries. Then it gets reduced to one value, which is returned to the client to combine.

###HBase
HBase is also a key-value store that is based on Google's Bigtable paper, which is somewhat the opposite of Riak. It gives you immediate consistency, but compromises on availability for reads and writes. HBase uses a master/slave model where only certain servers are able to write. 

I want to write more, but this blog post is getting way to long. So tune in next week as I go into HBase, document databases and graph databases!


[dataTalk]:http://opensourcebridge.org/sessions/557
[rcluster]:http://redis.io/topics/cluster-tutorial