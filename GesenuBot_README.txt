Interactive Intelligent Devices, System and Environments

Vacuum Cleaner Challenge 2k18


Francesco Gradi

GesenuBot & GesenuBotVAC


GesenuBot è il vacuum bot senza memoria. Il suo compito è quello di controllare lo sporco ad una distanza massima di 7 caselle e dirigervisi in caso lo trovi. In caso contrario, si ferma.

GesenuBotVAC invece è il vacuum bot con memoria limitata, ed è molto più elaborato. Oltre a controllare lo sporco fino ad una distanza massima di 10 caselle, lo controlla anche in diagonale e, nel caso lo trovi, si impone di dirigervisi al prossimo spostamento, a prescindere da qualsiasi altra casella sporca intorno.
Tutto il codice del suo movimento è racchiuso nella funzione Move(). La funzione Peek() gli permette di sbirciare nelle caselle accanto e nelle diagonali a distanza 1. La funzione NeverLoseHope() viene chiamata nel caso le 8 caselle adiacenti siano pulite oppure siano dei muri e gli permette di sbirciare caselle a distanza maggiore di 1.
Dopodiché, se non trova sporco nemmeno a caselle di distanza 10, viene chiamata la funzione BackRuler() che permette al bot di tornare indietro (fino ad un massimo di 6 caselle, come specificato dal contatore backCount) e soprattutto se nel tornare indietro incontra un muro, si dirige in una direzione casuale lungo di esso.
Infine la funzione FirstStepNoDirt() è utile nel caso in cui il bot nasca in un vicolo cieco in cui non vede sporco attorno a sè. Essa gli permette di uscirne e, sfruttando la funzione BackRuler(), di muoversi fino ad un massimo di 6 caselle nel caso non trovi sporco.