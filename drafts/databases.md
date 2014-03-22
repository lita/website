Title: Databases
Date: 2014-03-14
Slug: databases
Tags: databases, web, hacker school

I've been learning a lot about databases lately, and what sort of databases are out there currently. A fellow Hacker Schooler pointed me to a talk by Eric Redmond, which was pretty good of giving a generalized overview of whats out there. You can find the talk below:

[A Dozen Databases in 45 minutes][dataTalk]

After listening to this talk and talking with another Hacker Schooler about databases, I thought I share what I learned.

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

Another thing to mention is that you have to define a <b>schema</b> when you create your table, which defines what types of objects your database is going to store for that table. It's like defining your types in a static-type programming language. 

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

What's nice about a relational-database is that data is not duplicated everywhere. You can compute the table you need by using inner and outer joins. They are consistent and pretty reliable due to the fact that relational databases have been around for so long. 

The downsides are that relational databases are pretty inflexible. Because you have to define a schema ahead of time, you can't change what your database is going to store on the fly. However, you are guaranteed that the data will be what the schema says it will be. 

If you design your schema poorly, your database queries can get expensive. If you are doing a lot of joins to calculate your table, queries will take a long time.

Partitioning is also sucks with relational databases. You can't easily split out a part of a databases to different clusters. 

## Type: Key-Value Store  
#### Examples: Redis, Riak, HBase, memcached
Databases with the key-value model are basically hash tables. They store key-value pairs into your database. Because of the simplicity in the design, partitioning (horizontal scaling) is done really easily. By partitioning, I mean that one half of a database can live in one machine and the other half can live in another.

I've notice people using key-value stores (like memcached) in order to cache queries, but having their main database be relational. So they would distribute the popular queries in memcached in many servers, but of one server in charge of writing to the relational database.

During this portion of the talk, I also learned how <b>MapReduce</b> worked! I always thought of Hadoop and MapReduce as this fancy buzzword, but after Eric explained it, I felt silly not knowing about it sooner.

Lets say you have a partitioned key-value store in four servers. In this key-value, we store a username and age. We want to calculate the average age of all the users we have for our website. One way to go about it is to query four servers for all the users and manually calculate the average age on the client machine. But that would be REALLY slow. Why we just have the servers calculate the average age for all the data they have, and we can calculate the average age from the results? That is exactly what MapReduce does! We map the function to the servers, in which the servers run that function on each of their data-entries. Then it gets reduced to one value, which is returned to the client. 

## Type: Document Databases  
#### Examples: MongoDB, CouchDB
Document database are just collections of tables. I like to think of them how Microsoft Excel works. There are 2D tables and there are "Sheets", which are collections of tables. There are tons of duplicate data. The tables can't point to another table, like relational databases. 

## Graph Databases
#### Neo4J, Polyglot


[dataTalk]:http://opensourcebridge.org/sessions/557