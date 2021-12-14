from decsql import sql_statements

with sql_statements.declarations() as d:
    create_table = d.declare("create table foo (bar int, baz str)")
    save_foo = d.declare("insert into foo values (?, ?)")
    load_by_bar = d.declare("select * from foo where bar = :bar")


def main():
    import sqlite3

    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    create_table.run(cur)
    save_foo.run(cur, 3, "hello")
    save_foo.run(cur, 4, "goodbye")
    print((list(load_by_bar.run(cur, bar=3))))

main()
