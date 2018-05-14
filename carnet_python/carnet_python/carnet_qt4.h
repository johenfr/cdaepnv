#ifndef CARNET_QT4_H
#define CARNET_QT4_H

#if QT_VERSION >= 0x050000
#include <QtWidgets/QMainWindow>
#else
#include <QtGui/QMainWindow>
#endif

namespace Ui {
class Carnet_qt4;
}

class Carnet_qt4 : public QMainWindow
{
    Q_OBJECT

public:
    explicit Carnet_qt4(QWidget *parent = 0);
    ~Carnet_qt4();

private:
    Ui::Carnet_qt4 *ui;
};

#endif // CARNET_QT4_H
