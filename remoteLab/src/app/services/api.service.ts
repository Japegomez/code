import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, tap } from 'rxjs';
import { GetSessionConfigResponse } from '../interfaces/sessionConfig';

@Injectable({
  providedIn: 'root'
})
export class APIService {
  sessionConfig?: GetSessionConfigResponse;
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


  runLabConfig(typeCircuit: string, subtype: number) {
    return this.http.post('pi:5000/api/v1/lab/', {typeCircuit, subtype});
  }


}

