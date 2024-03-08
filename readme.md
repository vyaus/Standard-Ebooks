# Standard Ebooks

As of March 8, 2024, [Standard Ebooks](https://standardebooks.org/ebooks) offers a collection of 960 books, I have scraped all of the compatible epub books, and saved all of them in the format: `Author/Title/Title - Author.epub`. The path of the following 11 books include special characters, which are not permited on Windows system:

 - Ambrose Bierce/Can Such Things Be?
 - Anthony Trollope/Can You Forgive Her?
 - Dorothy L. Sayers/Whose Body?
 - Horatio Alger Jr./Ragged Dick
 - Karel Čapek/R.U.R.
 - Leo Tolstoy/What Is Art?
 - Philip Francis Nowlan/Armageddon 2419 A.D.
 - Pierre-Joseph Proudhon/What Is Property?
 - Richard Henry Dana Jr./To Cuba and Back
 - Richard Henry Dana Jr./Two Years Before the Mast
 - Washington Irving/The Sketch-Book of Geoffrey Crayon, Gent.

## Works Order by epub File Size

```sh
find . -type f -name "*.epub" -exec ls -lh {} + | sort -hr -k5 | head -n 30
```

File Size|Works|Author
-:|:-|-:
 60M|Seven Pillars of Wisdom|T. E. Lawrence
 42M|Nonsense Books|Edward Lear
 34M|Short Fiction|Beatrix Potter
 33M|Through the Looking-Glass|Lewis Carroll
 31M|Personal Memoirs of Ulysses S. Grant|Ulysses S. Grant
 20M|Twenty Years at Hull House|Jane Addams
 19M|The Path to Rome|Hilaire Belloc
 16M|Through the Brazilian Wilderness|Theodore Roosevelt
 16M|Alice’s Adventures in Wonderland|Lewis Carroll
9.1M|Just So Stories|Rudyard Kipling
8.9M|Ten Days That Shook the World|John Reed
7.0M|The Book of Wonder|Lord Dunsany
6.1M|My First Summer in the Sierra|John Muir
5.5M|An Autobiography|Theodore Roosevelt
5.5M|The History of the Decline and Fall of the Roman Empire|Edward Gibbon
5.2M|The Four Men|Hilaire Belloc
4.5M|Orlando|Virginia Woolf
4.1M|The Voyage of the Beagle|Charles Darwin
3.9M|A Negro Explorer at the North Pole|Matthew Henson
3.4M|The Diary|Samuel Pepys
3.4M|The Worst Journey in the World|Apsley Cherry-Garrard
3.0M|Clarissa|Samuel Richardson
3.0M|Short Fiction|O. Henry
2.9M|Les Misérables|Victor Hugo
2.8M|Dialogues|Plato
2.7M|Short Fiction|Guy de Maupassant
2.3M|In Search of Lost Time|Marcel Proust
2.3M|The Vicomte de Bragelonne|Alexandre Dumas
2.3M|War and Peace|Leo Tolstoy
2.3M|Short Fiction|Anton Chekhov

## Authors Order by Works Number

Author|Works Number
:-|:-
William Shakespeare|40
P. G. Wodehouse|23
Anthony Trollope|19
Edgar Rice Burroughs|17
Jules Verne|15
Edgar Wallace|15
Maurice Leblanc|12
Baroness Orczy|12
H. G. Wells|10
Charles Dickens|10
Arthur Conan Doyle|10
Leo Tolstoy|9
Jack London|9
G. K. Chesterton|9
E. Nesbit|9
Mark Twain|8
Andre Norton|8
Agatha Christie|8
Robert Louis Stevenson|7
Oscar Wilde|7
Virginia Woolf|6
Thomas Hardy|6
Jane Austen|6
James Branch Cabell|6
George Bernard Shaw|6
Fyodor Dostoevsky|6
Émile Gaboriau|5
Willa Cather|5
Wilkie Collins|5
W. Somerset Maugham|5
Margaret Oliphant|5
John Buchan|5
Honoré de Balzac|5
Henry James|5
H. Rider Haggard|5
H. Beam Piper|5
Ford Madox Ford|5
Dorothy L. Sayers|5
Alexandre Dumas|5
William Morris|4
Thomas Paine|4
Sinclair Lewis|4
Samuel Butler|4
Richard Jefferies|4
Lord Dunsany|4
Lewis Carroll|4
Joseph Conrad|4
James Stephens|4
J. S. Fletcher|4
Hilaire Belloc|4
Henryk Sienkiewicz|4
George MacDonald|4
George Eliot|4
Edith Wharton|4
E. M. Forster|4
Booth Tarkington|4
Arthur Machen|4
Ambrose Bierce|4
