export type GetMeasurementResponse = {
  data: {
    attributes: {
      current: Array<number>
      voltage: Array<number>
    }
    id: string
    type: string
  }
}