import readline
import textx as tx
import templateEngine as te

readline.write_history_file( '.lion_history' )
readline.set_history_length(1000)
mm = tx.metamodel_from_file('LION_META_MODEL.tx')

while(True):
    try : 
        c = input("lion> ")
        while(True) :
            if ';' in c:
                break
            c += input("...    ")
            
        m = mm.model_from_str(c)
        code = te.genCode(m)
        exec(code)
    except EOFError :
        print("\r   bye :(")
        break
    except KeyboardInterrupt:
        print("\ntype exit() or EOF to quit!")
    except SyntaxError as e:
        print("Invalid Syntax ERRROR", e)
    except Exception as e:
        print(e)