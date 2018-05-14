#include "carnet_qt4.h"
#include "ui_carnet_qt4.h"

Carnet_qt4::Carnet_qt4(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Carnet_qt4)
{
    ui->setupUi(this);
}

Carnet_qt4::~Carnet_qt4()
{
    delete ui;
}
