import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, tap } from 'rxjs';
import { GetMeasurementResponse } from '../interfaces/measurements';
import { GetSessionConfigResponse } from '../interfaces/sessionConfig';

@Injectable({
  providedIn: 'root'
})
export class APIService {
  sessionConfig?: GetSessionConfigResponse;
  measurements?: GetMeasurementResponse;
  constructor(private http: HttpClient ) { 
  }
  getSessionConfig(): Observable<GetSessionConfigResponse> {
    return this.http.get<GetSessionConfigResponse>('http://pi:5000/api/v1/config', {
      withCredentials: true
    }).pipe(
      tap((data: GetSessionConfigResponse) => {
        this.sessionConfig = data;
      })
    ); 
  }


  runLabConfig(typeCircuit: string, subtype: number): Observable<GetMeasurementResponse> {
    return this.http.get<GetMeasurementResponse>(`http://pi:5000/api/v1/lab/${typeCircuit}/${subtype}`, {
      withCredentials: true
    }).pipe(
      tap((data: GetMeasurementResponse) => {
        this.measurements = data;
      })
    );

  }


}

