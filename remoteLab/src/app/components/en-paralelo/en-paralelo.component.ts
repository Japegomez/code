import { NgClass } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { GetMeasurementResponse } from '../../interfaces/measurements';
import { APIService } from '../../services/api.service';
import { DynamicTableComponent } from '../dynamic-table/dynamic-table.component';
import { CameraViewerComponent } from "../camera-viewer/camera-viewer.component";

@Component({
    selector: 'app-en-paralelo',
    standalone: true,
    templateUrl: './en-paralelo.component.html',
    styleUrl: './en-paralelo.component.css',
    imports: [FormsModule, NgClass, DynamicTableComponent, CameraViewerComponent]
})
export class EnParaleloComponent {
  _numRamasEnParalelo = '2ramas';

  nombresColumnas = ["D1", "D2", "R1", "R2", "Rama1","Rama2","Total"];
  tensionData = [0,0,0,0,0,0,0];
  intensidadData = [0,0,0,0,0,0,0];
  valorR1: number | undefined;
  valorR2: number | undefined;
  valorR3: number | undefined;
  valorFuente = 5;
  isCorrect: boolean = false;

  constructor(private apiService: APIService) {
  }

  get numRamasEnParalelo() {
    return this._numRamasEnParalelo;
  }
  
  set numRamasEnParalelo(value: string) {
    this._numRamasEnParalelo = value;
    this.updateNombresColumnas();
    this.updateTensionData();
    this.updateIntensidadData();
  }

  updateNombresColumnas() {
  if (this._numRamasEnParalelo === '2ramas') {
    this.nombresColumnas = ["D1", "D2", "R1", "R2", "Rama 1","Rama 2","Total"];
  } 
  else {
    this.nombresColumnas = ["D1", "D2","D3", "R1", "R2","R3", "Rama1","Rama2","Rama3","Total"];
  }
  }

  updateTensionData() {
    if (this._numRamasEnParalelo === "2ramas") {
      this.tensionData = [0,0,0,0,0,0,0];
    }
    else {
      this.tensionData = [0,0,0,0,0,0,0,0,0,0];
    }
  }

  updateIntensidadData() {
    if (this._numRamasEnParalelo === "2ramas") {
      this.intensidadData = [0,0,0,0,0,0,0];
    }
    else {
      this.intensidadData = [0,0,0,0,0,0,0,0,0,0];
    }
  }

    updateValorFuente() {
    var isChecked = (<HTMLInputElement>document.getElementById("tensionFuente")).checked;
    if (isChecked) {
      this.valorFuente = 12;
    } else {
      this.valorFuente = 5;
    }
  }

  configLab() {
    if(this._numRamasEnParalelo==="2ramas") {
      if(this.valorFuente === 5) {
        if(this.valorR1 === 100 && this.valorR2 === 100){
          this.apiService.runLabConfig("C",1).subscribe((data: GetMeasurementResponse) => {
            this.tensionData = data.data.attributes.voltage;
            this.intensidadData = data.data.attributes.current;
          });
        }
        else if(this.valorR1 === 100 && this.valorR2 === 300){
          this.apiService.runLabConfig("C",2).subscribe((data: GetMeasurementResponse) => {
            this.tensionData = data.data.attributes.voltage;
            this.intensidadData = data.data.attributes.current;
          });
        }
      }
      if(this.valorFuente === 12) {
        if(this.valorR1 === 100 && this.valorR2 === 100){
          this.apiService.runLabConfig("C",3).subscribe((data: GetMeasurementResponse) => {
            this.tensionData = data.data.attributes.voltage;
            this.intensidadData = data.data.attributes.current;
          });
        }
        if(this.valorR1 === 100 && this.valorR2 === 300){
          this.apiService.runLabConfig("C",4).subscribe((data: GetMeasurementResponse) => {
            this.tensionData = data.data.attributes.voltage;
            this.intensidadData = data.data.attributes.current;
          });
        }
      }
    }
    if(this._numRamasEnParalelo==="3diodos") {
    }
  }
  checkValues() {
    if (this._numRamasEnParalelo === '2ramas') {
      if ((this.valorR1 === 100) && (this.valorR2 === 100 || this.valorR2 === 300)) {
        this.isCorrect = true;
      } else {
        this.isCorrect = false;
      }
    } else if (this._numRamasEnParalelo === '3ramas') {
      if ((this.valorR1 === 100 && this.valorR2===100 && this.valorR3 ===100) || (this.valorR1 === 100 && this.valorR2===100 && this.valorR3 ===300) || (this.valorR1 === 300 && this.valorR2===300 && this.valorR3 ===300) || (this.valorR1 === 300 && this.valorR2===300 && this.valorR3 ===100)){
        this.isCorrect = true;
      } else {
        this.isCorrect = false;
      }
    }
  }
}
