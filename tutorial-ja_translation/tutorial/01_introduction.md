.. _tutorial-introduction:

Introduction
============



Git自体と同様に、Dulwichは2つの主要なレイヤーで構成されています。 いわゆるplumbing と porcelain。

> Like Git itself, Dulwich consists of two main layers; the so-called plumbing and the porcelain.


plumbing は下位層であり、Gitオブジェクトデータベースと重要な内部を処理します。 porcelain は、大まかに `git` コマンドのようなツールのユーザーとして公開されると予想されるものです。

> The plumbing is the lower layer and it deals with the Git object database and the nitty gritty internals. The porcelain is roughly what you would expect to be exposed to as a user of the ``git`` command-like tool.

Dulwichには、かなり完全なplumbing の実装と、最近追加されたporcelain の実装があります。 磁器のコードは`dulwich.porcelain` にあります。


> Dulwich has a fairly complete plumbing implementation, and a more recently added porcelain implementation. The porcelain code lives in ``dulwich.porcelain``.


このチュートリアルでは、大部分について、Gitの内部概念とDulwichの主要なplumbing 部分を紹介します。 最後の章はporcelain をカバーしています。

> For the large part, this tutorial introduces you to the internal concepts of Git and the main plumbing parts of Dulwich. The last chapter covers the porcelain.
