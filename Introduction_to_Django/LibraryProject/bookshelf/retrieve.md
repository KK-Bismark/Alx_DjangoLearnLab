Book.objects.get(id=2)
Out[8]: <Book: Book object (2)>

In [9]: Book.objects.get(id=2)
Out[9]: <Book: Book object (2)>

In [10]: Book.__dict__
Out[10]: 
mappingproxy({'__module__': 'bookshelf.models',
              '__firstlineno__': 4,
              '__static_attributes__': (),
              '__doc__': 'Book(id, title, author, publication_year)',
              '_meta': <Options for Book>,
              'DoesNotExist': bookshelf.models.Book.DoesNotExist,
              'MultipleObjectsReturned': bookshelf.models.Book.MultipleObjectsReturned,
              'title': <django.db.models.query_utils.DeferredAttribute at 0x7f11f49f8f00>,
              'author': <django.db.models.query_utils.DeferredAttribute at 0x7f11f49f8f50>,
              'publication_year': <django.db.models.query_utils.DeferredAttribute at 0x7f11f49f8fa0>,
              'id': <django.db.models.query_utils.DeferredAttribute at 0x7f11f49f8eb0>,
              'objects': <django.db.models.manager.ManagerDescriptor at 0x7f11f4f43e30>})
