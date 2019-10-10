# find_the_site
## Are you looking for a company/enterprise website? This small library finds websites in [duckduckgo search engine](https://duckduckgo.com/?t=hk)
#### Optionally you can use:
- the [ecosia](https://ecosia.org) search engine, to support environmental efforts
##### How to Install ?

```
pip install find_the_site
```

##### How to use ?

def get_website(website, eco=False)
> **website**: Whose website you are searching for
>
> **eco**: 
>- **True**: Use ecosia search.
>- **default**: **False**

##### Find the website

```
In [1]: from find_the_site.fw import get_website                                               

In [2]: get_website("UNITED NATIONS")                                                          
Out[2]: 'https://www.un.org/en/'
```
#
```
In [1]: from find_the_site.fw import get_website 

In [2]: get_website("UNITED NATIONS", eco=True)                                                          
Out[2]: 'https://www.un.org/en/'
```
