Encoding
========


Dulwichのすべての下位レベルの関数は、Unicode文字列ではなくバイト文字列を取ることに気づくでしょう。 これは意図的なものです。


> You will notice that all lower-level functions in Dulwich take byte strings rather than unicode strings. This is intentional.

`C git` はエンコーディングにUTF-8の使用を推奨していますが、これは厳密に強制されておらず、`C git` はファイル名を非NULバイトのシーケンスとして扱います。
ファイル名とコミットメッセージに非UTF-8エンコーディングを使用するリポジトリが一般にあります。


[C git](https://github.com/git/git/blob/master/Documentation/i18n.txt)


> Although `C git`_ recommends the use of UTF-8 for encoding, this is not strictly enforced and C git treats filenames as sequences of non-NUL bytes.
> There are repositories in the wild that use non-UTF-8 encoding for filenames and commit messages.

> .. _C git: https://github.com/git/git/blob/master/Documentation/i18n.txt


ライブラリは、使用するエンコーディングに関係なく、*すべての*既存のgitリポジトリを読み取ることができる必要があります。これが、DulwichがパスをUnicode文字列に変換しない主な理由です。


> The library should be able to read *all* existing git repositories, irregardless of what encoding they use. This is the main reason why Dulwich does not convert paths to unicode strings.


さらに考慮しなければならないのは、ユニコードへの変換を行ったり来たりすると、パフォーマンスがさらに低下することです。
例えば : ファイルの内容を反復するだけの場合は、エンコードされた文字列を考慮する必要はありません。 ライブラリのユーザーは、エンコードに関して特定の前提条件を持っている可能性があります。 すべてのデータがラテン-1、つまりデフォルトのPythonエンコーディングであると判断するだけです。


> A further consideration is that converting back and forth to unicode is an extra performance penalty. E.g. if you are just iterating over file contents, there is no need to consider encoded strings. Users of the library may have specific assumptions they can make about the encoding - e.g. they could just decide that all their data is latin-1, or the default Python encoding.

dulwich.porcelainのporcelain などの上位レベルの関数は、Unicode文字列を自動的にUTF-8バイト文字列に変換します。


> Higher level functions, such as the porcelain in dulwich.porcelain, will automatically convert unicode strings to UTF-8 bytestrings.

