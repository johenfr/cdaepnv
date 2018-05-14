#include "carnet_qt4.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Carnet_qt4 w;
    w.show();

    return a.exec();
}
