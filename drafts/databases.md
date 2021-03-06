Title: Databases
Date: 2014-03-14
Slug: databases
Tags: databases, web, hacker school

I've been learning a lot about databases lately, and what sort of databases are out there currently. A fellow Hacker Schooler pointed me to a talk by Eric Redmond, which was pretty good of giving a generalized overview of whats out there. You can find the talk below:

[A Dozen Databases in 45 minutes][dataTalk]

After listening to this talk and talking with another Hacker Schooler about databases, I thought I share what I learned. I am mostly going to go deeper with Open Source databases, so anyone can try using them at home.

## Type: Relational Databases  
#### Examples: MySQL, PostgreSQL  
This is the most common database out there. It has been around for a long time and very mature. You have a collection of 2D tables (rows and columns), very similar to Excel spreadsheets. However, you can add relationships between tables. Lets say you have the following two tables.

<table style="width:400px">
<tr>
  <th>name</th>
  <th>postal_code</th>     
  <th>country_code</th>
  </tr>
<tr>
<tr>
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
<tr>
<tr>
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

You can create a relationship between the two tables by using the "country_code" attribute as your key. I prefer to think of these relational attributes as pointers to different tables.

![Table Example](/images/table.png)
<p class=subnote> Note: Image taken from <u>Seven Databases in Seven Weeks</u> by Eric Redmond and Jim R. Wilson </p>

You have to define a <b>schema</b> when you create your table, which defines what types of objects your database is going to store for that table. It's like defining your types in a static-type programming language. This can be annoying, since you have to architect your data ahead of time.

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
 
Because of the schema, relational databases are strict with what kind of data you put in them. If you define the 'dob' as "date", it has to take in a particular format MM/DD/YYYY. If you try to input a string or random numbers, the database will throw an error.

What's nice and powerful about a relational-database are the queries you can make. You can use SQL to create new tables based on inner and out joins. Lets say you have two tables and you jus

You can compute the table you need by using inner and outer joins. They are consistent and pretty reliable due to the fact that relational databases have been around for so long. 

The downsides are that relational databases are pretty inflexible. Because you have to define a schema ahead of time, you can't change what your database is going to store on the fly. However, you are guaranteed that the data will be what the schema says it will be. 

If you design your schema poorly, your database queries can get expensive. If you are doing a lot of joins to calculate your table, queries will take a long time. I can see as your website grows, it would be a lot of work to refactor your schema as your needs change.

Partitioning is also sucks with relational databases. As your database grows, you can't just split your database in half and put it somewhere else. Because relational databases can point to other tables, you would need to replicate the database intelligently. 

A lot of relational-databases do **sharding** to scale to multiple servers, which is a fancy term for splitting up the rows of the table in some logical way to different servers. 

![Sharding Example][/images/sharding.jpg]
<p class=subnote> Crude, but awesome, example of sharding! Imagine this table has only one column and holds rows 'eggs, other crap, dogs, and fish'. Now dogs and fish are split out to they own separate servers, while egg and crap are within their own servers.
<p class=subnote> Note: Image taking from Shai Wininger from his <a href="http://hackingshmacking.com/tag/haproxy/">blog entry</a>.

However, figuring out how to split up your data in a relational database is not trivial. You will also need to write sharding code, also known as a load balancer, that manages where your data goes. Handing JOINS and UNIONS also get super complicated. Overall, it is a lot of work to scale a relational database.

There are systems that do auto-sharding, like MySQL Cluster. But overall, relational databases get non-linear pretty quickly, causing latency issues, especially if your schema aren't designed well. Overall, there are better solutions out there if you know your database is going to grow massively.

## Type: Key-Value Store  
#### Examples: Riak, HBase, Redis, memcached
Databases with the key-value model are basically store data based on a key, which is VERY similar to a hash table. Because of the simplicity in the design, partitioning (horizontal scaling) is done really easily. Just split the data based on the hash function. 

However, with memcached and Redis, all the data lives in RAM. Because of this, both databases are incredibly fast at reads and writes. Redis can write to disk if it ever shuts down, so it stays persistence, but can't read from disk while its on. Memcached doesn't do this, so the data is lost when it shuts down. Redis is currently working on [clustering in order to make it scalable][rcluster], but it is in its alpha stages. Overall, I wouldn't use these databases as your main data store unless you are working on something small. Rather I would complement your web app with another database, like Riak, HBase or another relational/document database.

Speaking Riak and HBase, lets get into these key-value stores! 

I've notice people using key-value stores (like memcached) in order to cache queries, but having their main database be relational. So they would distribute the popular queries in memcached in many servers, but of one server in charge of writing to the relational database.

During this portion of the talk, I also learned how <b>MapReduce</b> worked! I always thought of Hadoop and MapReduce as this fancy buzzword, but after Eric explained it, I felt silly not knowing about it sooner.

Lets say you have a partitioned key-value store in four servers. In this key-value, we store a username and age. We want to calculate the average age of all the users we have for our website. One way to go about it is to query four servers for all the users and manually calculate the average age on the client machine. But that would be REALLY slow. Why we just have the servers calculate the average age for all the data they have, and we can calculate the average age from the results? That is exactly what MapReduce does! We map the function to the servers, in which the servers run that function on each of their data-entries. Then it gets reduced to one value, which is returned to the client. 

## Type: Document Databases  
#### Examples: MongoDB, CouchDB
Document database are just collections of tables. I like to think of them how Microsoft Excel works. There are 2D tables and there are "Sheets", which are collections of tables. There are tons of duplicate data. The tables can't point to another table, like relational databases. 

## Graph Databases
#### Neo4J, Polyglot


[dataTalk]:http://opensourcebridge.org/sessions/557
[rcluster]:http://redis.io/topics/cluster-tutorial