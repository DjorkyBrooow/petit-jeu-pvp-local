import Etat
import Direction


class Classe:

    pv_max : int
    pv_actuel: int
    mobi: int
    deg: int
    portee: int
    etat: Etat
    direc: Direction
    en_vie: bool
    nom: str

	PV_FAIBLE: Final = 13;
	public static final int PV_MOYEN = 16;
	public static final int PV_ELEVE= 20;
	public static final int DEGAT_FAIBLE = 1;
	public static final int DEGAT_MOYEN= 2;
	public static final int DEGAT_ELEVE = 3;
	public static final int MOBILITE_FAIBLE = 3;
	public static final int MOBILITE_MOYENNE = 4;
	public static final int MOBILITE_ELEVEE= 5;
	public static final int CORPS_A_CORPS = 1;
	public static final int A_DISTANCE = 7;

    def __init__(self) -> None:

        pass