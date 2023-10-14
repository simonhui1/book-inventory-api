package com.simonhui.bookinventory.model; // This should match your package path

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity  // This annotation tells Spring that this class is an entity (i.e., a table in our database).
public class Book {

    @Id  // This annotation tells Spring that the 'id' field is the primary key for this table.
    @GeneratedValue(strategy = GenerationType.IDENTITY)  // This auto-generates a unique value for each new entry.
    private Long id;
    private String title;
    private String author;
    private String isbn;
    private Date publishedDate;

    // For now, we will keep it this simple. We'll add constructors, getters, setters, and other methods later.
}
