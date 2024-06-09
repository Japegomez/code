import { Component } from '@angular/core';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { GetSessionConfigResponse } from '../../interfaces/sessionConfig';
import { APIService } from '../../services/api.service';
import { EnParaleloComponent } from '../en-paralelo/en-paralelo.component';
import { EnSerieComponent } from '../en-serie/en-serie.component';
import { SerieYParaleloComponent } from '../serie-yparalelo/serie-yparalelo.component';
import { TimerComponent } from '../timer/timer.component';
import { ToggleButtonComponent } from '../toggle-button/toggle-button.component';

@Component({
  selector: 'app-laboratory',
  standalone: true,
  imports: [TimerComponent, ToggleButtonComponent, EnSerieComponent, EnParaleloComponent, MatProgressSpinnerModule, SerieYParaleloComponent],
  templateUrl: './laboratory.component.html',
  styleUrl: './laboratory.component.css'
})
export class LaboratoryComponent {
  title = 'LabRemoto';
  tipoCircuito = "EnSerie";
  username = ""
  tiempoRestante = 0;
  
  constructor(private apiService: APIService) {
  }
  ngOnInit() {
    this.apiService.getSessionConfig().subscribe((data: GetSessionConfigResponse) => {
      const user = data.included.find(e => e.id === data.data.relationships.user.data.id);
      if (!user){
        return;
      } 

      this.username = user.attributes.name;
      this.tiempoRestante = data.data.attributes.assigned_time;
    }
    );
  }
  setTipoCircuito(tipo: string) {
    this.tipoCircuito = tipo;
  }
  logout(){
    this.apiService.logout().subscribe();
  }
}

