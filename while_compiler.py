class WhileCompiler:

    def __init__(self, source):
        self.source = source
        self.label = 1

    def new_label(self):
        lbl = f"L{self.label}"
        self.label += 1
        return lbl

    def lexical_analysis(self):

        tokens = self.source

        for ch in ['(', ')', '{', '}', '<', '=', '+']:
            tokens = tokens.replace(ch, f' {ch} ')

        return tokens.split()

    def syntax_analysis(self, tokens):

        if tokens[0] != 'while':
            raise SyntaxError("Expected while")

        idx1 = tokens.index('(')
        idx2 = tokens.index(')')

        condition = tokens[idx1+1:idx2]

        start_body = tokens.index('{')
        end_body = tokens.index('}')

        body = tokens[start_body+1:end_body]

        return condition, body

    def semantic_analysis(self, condition, body):

        symbol_table = {
            'x': 'int'
        }

        variable = condition[0]

        if variable not in symbol_table:
            raise Exception("Semantic Error")

        return True

    def generate_tac(self):

        tokens = self.lexical_analysis()

        condition, body = self.syntax_analysis(tokens)

        self.semantic_analysis(condition, body)

        begin = self.new_label()
        end = self.new_label()

        tac = []

        tac.append(begin + ":")

        cond = " ".join(condition)

        tac.append(
            f"ifFalse {cond} goto {end}"
        )

        statement = " ".join(body)

        tac.append(statement)

        tac.append(
            f"goto {begin}"
        )

        tac.append(end + ":")

        return tac


source = """
while ( x < 10 )
{
x = x + 1
}
"""

compiler = WhileCompiler(source)

print("=== TOKENS ===")
print(compiler.lexical_analysis())

print()

print("=== THREE ADDRESS CODE ===")

for line in compiler.generate_tac():
    print(line)