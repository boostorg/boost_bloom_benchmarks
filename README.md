# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.02</td>
    <td align="right">4.80</td>
    <td align="right">3.64</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">10.98</td>
    <td align="right">10.56</td>
    <td align="right">16.71</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.00</td>
    <td align="right">4.35</td>
    <td align="right">4.36</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.92</td>
    <td align="right">5.03</td>
    <td align="right">5.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.38</td>
    <td align="right">15.52</td>
    <td align="right">17.55</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.78</td>
    <td align="right">4.91</td>
    <td align="right">4.96</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.41</td>
    <td align="right">5.49</td>
    <td align="right">5.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.03</td>
    <td align="right">18.54</td>
    <td align="right">16.47</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.39</td>
    <td align="right">5.34</td>
    <td align="right">5.31</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.21</td>
    <td align="right">6.25</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.11</td>
    <td align="right">22.66</td>
    <td align="right">16.96</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">7.11</td>
    <td align="right">5.90</td>
    <td align="right">5.89</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.75</td>
    <td align="right">6.56</td>
    <td align="right">6.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.05</td>
    <td align="right">5.72</td>
    <td align="right">5.79</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.25</td>
    <td align="right">6.55</td>
    <td align="right">6.49</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.95</td>
    <td align="right">3.26</td>
    <td align="right">3.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.48</td>
    <td align="right">8.81</td>
    <td align="right">8.81</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.14</td>
    <td align="right">9.82</td>
    <td align="right">9.88</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.47</td>
    <td align="right">3.12</td>
    <td align="right">3.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.25</td>
    <td align="right">13.71</td>
    <td align="right">13.72</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.86</td>
    <td align="right">14.10</td>
    <td align="right">14.07</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.77</td>
    <td align="right">5.80</td>
    <td align="right">3.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.14</td>
    <td align="right">15.57</td>
    <td align="right">15.52</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.65</td>
    <td align="right">17.50</td>
    <td align="right">17.53</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.98</td>
    <td align="right">5.89</td>
    <td align="right">3.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.06</td>
    <td align="right">3.35</td>
    <td align="right">3.24</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.47</td>
    <td align="right">5.23</td>
    <td align="right">5.16</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.52</td>
    <td align="right">5.10</td>
    <td align="right">5.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.13</td>
    <td align="right">3.27</td>
    <td align="right">3.46</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.29</td>
    <td align="right">4.44</td>
    <td align="right">4.50</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.60</td>
    <td align="right">5.21</td>
    <td align="right">5.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.65</td>
    <td align="right">5.76</td>
    <td align="right">3.91</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.19</td>
    <td align="right">7.96</td>
    <td align="right">5.92</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.95</td>
    <td align="right">7.76</td>
    <td align="right">5.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.45</td>
    <td align="right">5.85</td>
    <td align="right">3.92</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">7.96</td>
    <td align="right">9.33</td>
    <td align="right">6.16</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.27</td>
    <td align="right">9.32</td>
    <td align="right">6.01</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.78</td>
    <td align="right">21.90</td>
    <td align="right">21.57</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.93</td>
    <td align="right">14.81</td>
    <td align="right">14.76</td>
    <td align="center">5</td>
    <td align="right">2.2514</td>
    <td align="right">10.94</td>
    <td align="right">18.44</td>
    <td align="right">18.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4119</td>
    <td align="right">10.07</td>
    <td align="right">22.71</td>
    <td align="right">23.13</td>
    <td align="center">8</td>
    <td align="right">0.4119</td>
    <td align="right">10.49</td>
    <td align="right">18.14</td>
    <td align="right">18.17</td>
    <td align="center">8</td>
    <td align="right">0.3831</td>
    <td align="right">13.14</td>
    <td align="right">21.63</td>
    <td align="right">21.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0844</td>
    <td align="right">13.80</td>
    <td align="right">24.91</td>
    <td align="right">24.61</td>
    <td align="center">11</td>
    <td align="right">0.0844</td>
    <td align="right">13.90</td>
    <td align="right">26.01</td>
    <td align="right">25.98</td>
    <td align="center">11</td>
    <td align="right">0.0739</td>
    <td align="right">17.13</td>
    <td align="right">22.66</td>
    <td align="right">22.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0213</td>
    <td align="right">15.02</td>
    <td align="right">25.02</td>
    <td align="right">25.03</td>
    <td align="center">13</td>
    <td align="right">0.0213</td>
    <td align="right">15.23</td>
    <td align="right">19.23</td>
    <td align="right">19.20</td>
    <td align="center">14</td>
    <td align="right">0.0165</td>
    <td align="right">19.49</td>
    <td align="right">25.36</td>
    <td align="right">25.21</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">34.58</td>
    <td align="right">22.33</td>
    <td align="right">8.90</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">16.94</td>
    <td align="right">13.45</td>
    <td align="right">18.01</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.79</td>
    <td align="right">5.09</td>
    <td align="right">5.10</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.85</td>
    <td align="right">6.01</td>
    <td align="right">6.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.58</td>
    <td align="right">18.30</td>
    <td align="right">18.41</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.40</td>
    <td align="right">5.54</td>
    <td align="right">5.66</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.21</td>
    <td align="right">6.31</td>
    <td align="right">6.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">30.40</td>
    <td align="right">33.67</td>
    <td align="right">19.50</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.86</td>
    <td align="right">10.69</td>
    <td align="right">6.22</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.57</td>
    <td align="right">7.66</td>
    <td align="right">7.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">39.70</td>
    <td align="right">40.03</td>
    <td align="right">19.88</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">10.85</td>
    <td align="right">10.25</td>
    <td align="right">13.42</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">12.95</td>
    <td align="right">12.51</td>
    <td align="right">14.19</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.32</td>
    <td align="right">7.05</td>
    <td align="right">7.23</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.00</td>
    <td align="right">8.29</td>
    <td align="right">8.10</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.64</td>
    <td align="right">4.17</td>
    <td align="right">4.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.41</td>
    <td align="right">10.53</td>
    <td align="right">10.63</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">14.54</td>
    <td align="right">16.17</td>
    <td align="right">16.23</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">6.94</td>
    <td align="right">3.77</td>
    <td align="right">3.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">15.03</td>
    <td align="right">17.18</td>
    <td align="right">16.91</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">20.70</td>
    <td align="right">16.57</td>
    <td align="right">16.10</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.97</td>
    <td align="right">15.94</td>
    <td align="right">5.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">30.35</td>
    <td align="right">24.09</td>
    <td align="right">19.70</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">15.36</td>
    <td align="right">21.07</td>
    <td align="right">23.82</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">9.35</td>
    <td align="right">12.16</td>
    <td align="right">6.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.54</td>
    <td align="right">4.08</td>
    <td align="right">4.09</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.27</td>
    <td align="right">6.25</td>
    <td align="right">6.08</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.42</td>
    <td align="right">6.05</td>
    <td align="right">6.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.52</td>
    <td align="right">4.21</td>
    <td align="right">4.00</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.67</td>
    <td align="right">5.05</td>
    <td align="right">5.05</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">5.07</td>
    <td align="right">6.02</td>
    <td align="right">6.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.37</td>
    <td align="right">6.84</td>
    <td align="right">4.99</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">8.97</td>
    <td align="right">9.40</td>
    <td align="right">7.57</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.19</td>
    <td align="right">9.26</td>
    <td align="right">7.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.86</td>
    <td align="right">10.81</td>
    <td align="right">7.67</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">22.49</td>
    <td align="right">12.73</td>
    <td align="right">8.66</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.53</td>
    <td align="right">13.29</td>
    <td align="right">9.93</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.23</td>
    <td align="right">26.17</td>
    <td align="right">25.33</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.26</td>
    <td align="right">16.79</td>
    <td align="right">16.69</td>
    <td align="center">5</td>
    <td align="right">2.2818</td>
    <td align="right">11.72</td>
    <td align="right">20.90</td>
    <td align="right">20.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4140</td>
    <td align="right">11.06</td>
    <td align="right">24.68</td>
    <td align="right">24.74</td>
    <td align="center">8</td>
    <td align="right">0.4140</td>
    <td align="right">11.44</td>
    <td align="right">18.32</td>
    <td align="right">18.32</td>
    <td align="center">8</td>
    <td align="right">0.3795</td>
    <td align="right">14.09</td>
    <td align="right">23.30</td>
    <td align="right">23.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0895</td>
    <td align="right">16.41</td>
    <td align="right">28.03</td>
    <td align="right">29.72</td>
    <td align="center">11</td>
    <td align="right">0.0895</td>
    <td align="right">16.42</td>
    <td align="right">26.67</td>
    <td align="right">26.39</td>
    <td align="center">11</td>
    <td align="right">0.0721</td>
    <td align="right">19.39</td>
    <td align="right">25.23</td>
    <td align="right">25.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0212</td>
    <td align="right">19.01</td>
    <td align="right">30.93</td>
    <td align="right">33.76</td>
    <td align="center">13</td>
    <td align="right">0.0212</td>
    <td align="right">20.59</td>
    <td align="right">23.36</td>
    <td align="right">23.90</td>
    <td align="center">14</td>
    <td align="right">0.0165</td>
    <td align="right">28.38</td>
    <td align="right">54.57</td>
    <td align="right">53.41</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.61</td>
    <td align="right">4.32</td>
    <td align="right">3.44</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">8.62</td>
    <td align="right">8.21</td>
    <td align="right">14.72</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.18</td>
    <td align="right">3.73</td>
    <td align="right">3.87</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.78</td>
    <td align="right">4.43</td>
    <td align="right">4.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.58</td>
    <td align="right">12.47</td>
    <td align="right">15.84</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.65</td>
    <td align="right">4.33</td>
    <td align="right">4.48</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.30</td>
    <td align="right">5.27</td>
    <td align="right">5.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.66</td>
    <td align="right">15.04</td>
    <td align="right">14.96</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.10</td>
    <td align="right">4.83</td>
    <td align="right">4.88</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.87</td>
    <td align="right">5.86</td>
    <td align="right">5.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.40</td>
    <td align="right">18.77</td>
    <td align="right">15.40</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.80</td>
    <td align="right">5.50</td>
    <td align="right">5.51</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.68</td>
    <td align="right">3.07</td>
    <td align="right">3.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.91</td>
    <td align="right">3.41</td>
    <td align="right">3.40</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.01</td>
    <td align="right">3.30</td>
    <td align="right">3.31</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.44</td>
    <td align="right">2.36</td>
    <td align="right">2.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.55</td>
    <td align="right">3.86</td>
    <td align="right">3.90</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.45</td>
    <td align="right">4.14</td>
    <td align="right">4.14</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.00</td>
    <td align="right">2.16</td>
    <td align="right">2.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.19</td>
    <td align="right">6.66</td>
    <td align="right">6.69</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.41</td>
    <td align="right">6.54</td>
    <td align="right">6.56</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.91</td>
    <td align="right">4.12</td>
    <td align="right">2.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.63</td>
    <td align="right">7.28</td>
    <td align="right">7.29</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.91</td>
    <td align="right">7.76</td>
    <td align="right">7.69</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.94</td>
    <td align="right">4.13</td>
    <td align="right">2.95</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.47</td>
    <td align="right">2.21</td>
    <td align="right">2.22</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.38</td>
    <td align="right">3.88</td>
    <td align="right">3.85</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.56</td>
    <td align="right">3.72</td>
    <td align="right">3.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.54</td>
    <td align="right">2.26</td>
    <td align="right">2.27</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.69</td>
    <td align="right">3.52</td>
    <td align="right">3.55</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.60</td>
    <td align="right">3.79</td>
    <td align="right">3.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.95</td>
    <td align="right">4.00</td>
    <td align="right">2.79</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.20</td>
    <td align="right">5.77</td>
    <td align="right">4.76</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.36</td>
    <td align="right">5.58</td>
    <td align="right">4.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">3.96</td>
    <td align="right">4.02</td>
    <td align="right">2.73</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.41</td>
    <td align="right">6.82</td>
    <td align="right">4.53</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.54</td>
    <td align="right">6.74</td>
    <td align="right">5.05</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.41</td>
    <td align="right">13.74</td>
    <td align="right">13.76</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.49</td>
    <td align="right">14.12</td>
    <td align="right">14.12</td>
    <td align="center">5</td>
    <td align="right">2.2514</td>
    <td align="right">11.80</td>
    <td align="right">14.21</td>
    <td align="right">14.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4119</td>
    <td align="right">9.44</td>
    <td align="right">15.42</td>
    <td align="right">15.62</td>
    <td align="center">8</td>
    <td align="right">0.4119</td>
    <td align="right">10.03</td>
    <td align="right">16.05</td>
    <td align="right">16.07</td>
    <td align="center">8</td>
    <td align="right">0.3831</td>
    <td align="right">12.27</td>
    <td align="right">16.14</td>
    <td align="right">16.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0844</td>
    <td align="right">12.11</td>
    <td align="right">17.51</td>
    <td align="right">17.56</td>
    <td align="center">11</td>
    <td align="right">0.0844</td>
    <td align="right">13.14</td>
    <td align="right">17.00</td>
    <td align="right">17.02</td>
    <td align="center">11</td>
    <td align="right">0.0739</td>
    <td align="right">16.19</td>
    <td align="right">16.99</td>
    <td align="right">17.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0213</td>
    <td align="right">14.54</td>
    <td align="right">17.53</td>
    <td align="right">17.53</td>
    <td align="center">13</td>
    <td align="right">0.0213</td>
    <td align="right">14.80</td>
    <td align="right">17.80</td>
    <td align="right">17.82</td>
    <td align="center">14</td>
    <td align="right">0.0165</td>
    <td align="right">18.63</td>
    <td align="right">18.54</td>
    <td align="right">18.51</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">35.15</td>
    <td align="right">16.96</td>
    <td align="right">8.37</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.12</td>
    <td align="right">10.61</td>
    <td align="right">16.27</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.77</td>
    <td align="right">4.25</td>
    <td align="right">4.34</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.58</td>
    <td align="right">5.38</td>
    <td align="right">5.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">14.11</td>
    <td align="right">14.18</td>
    <td align="right">16.85</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.43</td>
    <td align="right">6.35</td>
    <td align="right">5.96</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">4.82</td>
    <td align="right">5.72</td>
    <td align="right">5.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">29.67</td>
    <td align="right">31.51</td>
    <td align="right">18.20</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">7.72</td>
    <td align="right">8.72</td>
    <td align="right">7.95</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.45</td>
    <td align="right">11.00</td>
    <td align="right">11.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">61.86</td>
    <td align="right">66.66</td>
    <td align="right">23.23</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">14.14</td>
    <td align="right">16.11</td>
    <td align="right">15.79</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.94</td>
    <td align="right">10.98</td>
    <td align="right">10.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.66</td>
    <td align="right">4.29</td>
    <td align="right">4.31</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.86</td>
    <td align="right">4.28</td>
    <td align="right">4.22</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.17</td>
    <td align="right">3.07</td>
    <td align="right">3.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.46</td>
    <td align="right">5.42</td>
    <td align="right">5.15</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.25</td>
    <td align="right">5.39</td>
    <td align="right">5.55</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.92</td>
    <td align="right">3.09</td>
    <td align="right">2.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">9.54</td>
    <td align="right">14.16</td>
    <td align="right">13.06</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">9.93</td>
    <td align="right">13.93</td>
    <td align="right">15.98</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">9.90</td>
    <td align="right">14.90</td>
    <td align="right">9.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">18.96</td>
    <td align="right">24.67</td>
    <td align="right">21.52</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.84</td>
    <td align="right">23.04</td>
    <td align="right">21.09</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">12.01</td>
    <td align="right">14.26</td>
    <td align="right">10.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.10</td>
    <td align="right">2.93</td>
    <td align="right">2.90</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.26</td>
    <td align="right">5.18</td>
    <td align="right">5.27</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.45</td>
    <td align="right">4.86</td>
    <td align="right">4.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.49</td>
    <td align="right">3.39</td>
    <td align="right">3.26</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">6.03</td>
    <td align="right">7.64</td>
    <td align="right">7.08</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">6.63</td>
    <td align="right">5.35</td>
    <td align="right">5.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">10.97</td>
    <td align="right">12.14</td>
    <td align="right">8.27</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">10.32</td>
    <td align="right">11.96</td>
    <td align="right">9.98</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">10.38</td>
    <td align="right">10.94</td>
    <td align="right">8.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">14.34</td>
    <td align="right">16.24</td>
    <td align="right">9.62</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">15.95</td>
    <td align="right">17.62</td>
    <td align="right">15.22</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">18.69</td>
    <td align="right">19.40</td>
    <td align="right">12.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.19</td>
    <td align="right">16.15</td>
    <td align="right">15.88</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.46</td>
    <td align="right">17.20</td>
    <td align="right">17.02</td>
    <td align="center">5</td>
    <td align="right">2.2818</td>
    <td align="right">13.00</td>
    <td align="right">17.59</td>
    <td align="right">17.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4140</td>
    <td align="right">20.37</td>
    <td align="right">25.20</td>
    <td align="right">22.30</td>
    <td align="center">8</td>
    <td align="right">0.4140</td>
    <td align="right">14.89</td>
    <td align="right">19.01</td>
    <td align="right">20.97</td>
    <td align="center">8</td>
    <td align="right">0.3795</td>
    <td align="right">20.43</td>
    <td align="right">25.58</td>
    <td align="right">22.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0895</td>
    <td align="right">37.83</td>
    <td align="right">37.26</td>
    <td align="right">34.76</td>
    <td align="center">11</td>
    <td align="right">0.0895</td>
    <td align="right">35.61</td>
    <td align="right">29.32</td>
    <td align="right">31.59</td>
    <td align="center">11</td>
    <td align="right">0.0721</td>
    <td align="right">54.16</td>
    <td align="right">32.44</td>
    <td align="right">31.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0212</td>
    <td align="right">46.59</td>
    <td align="right">35.15</td>
    <td align="right">36.49</td>
    <td align="center">13</td>
    <td align="right">0.0212</td>
    <td align="right">44.77</td>
    <td align="right">39.18</td>
    <td align="right">41.00</td>
    <td align="center">14</td>
    <td align="right">0.0165</td>
    <td align="right">57.89</td>
    <td align="right">41.59</td>
    <td align="right">40.79</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.47</td>
    <td align="right">7.08</td>
    <td align="right">4.64</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">8.53</td>
    <td align="right">5.61</td>
    <td align="right">13.26</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.44</td>
    <td align="right">1.31</td>
    <td align="right">1.31</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">2.18</td>
    <td align="right">1.44</td>
    <td align="right">1.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.90</td>
    <td align="right">11.84</td>
    <td align="right">14.75</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.82</td>
    <td align="right">1.78</td>
    <td align="right">1.79</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">2.04</td>
    <td align="right">1.65</td>
    <td align="right">1.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.32</td>
    <td align="right">11.88</td>
    <td align="right">13.58</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.96</td>
    <td align="right">2.38</td>
    <td align="right">2.02</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">2.31</td>
    <td align="right">1.93</td>
    <td align="right">1.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">22.98</td>
    <td align="right">18.57</td>
    <td align="right">16.89</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.54</td>
    <td align="right">3.05</td>
    <td align="right">3.74</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.36</td>
    <td align="right">2.85</td>
    <td align="right">2.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.71</td>
    <td align="right">2.19</td>
    <td align="right">1.91</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.94</td>
    <td align="right">2.01</td>
    <td align="right">2.28</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.29</td>
    <td align="right">1.97</td>
    <td align="right">1.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.61</td>
    <td align="right">2.36</td>
    <td align="right">2.39</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.10</td>
    <td align="right">3.61</td>
    <td align="right">2.53</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.83</td>
    <td align="right">1.70</td>
    <td align="right">1.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.22</td>
    <td align="right">3.75</td>
    <td align="right">3.74</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.60</td>
    <td align="right">3.92</td>
    <td align="right">4.21</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.90</td>
    <td align="right">3.24</td>
    <td align="right">2.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.66</td>
    <td align="right">5.19</td>
    <td align="right">4.38</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.56</td>
    <td align="right">5.80</td>
    <td align="right">4.92</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.41</td>
    <td align="right">3.98</td>
    <td align="right">2.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.26</td>
    <td align="right">2.15</td>
    <td align="right">2.45</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.77</td>
    <td align="right">1.94</td>
    <td align="right">2.11</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.66</td>
    <td align="right">2.21</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.95</td>
    <td align="right">1.85</td>
    <td align="right">2.12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.30</td>
    <td align="right">2.43</td>
    <td align="right">2.48</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.51</td>
    <td align="right">2.61</td>
    <td align="right">2.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.93</td>
    <td align="right">3.38</td>
    <td align="right">2.12</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.55</td>
    <td align="right">4.39</td>
    <td align="right">3.51</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.62</td>
    <td align="right">4.52</td>
    <td align="right">3.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.44</td>
    <td align="right">4.77</td>
    <td align="right">2.91</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.57</td>
    <td align="right">4.24</td>
    <td align="right">4.77</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.59</td>
    <td align="right">4.80</td>
    <td align="right">5.64</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">4.11</td>
    <td align="right">10.17</td>
    <td align="right">9.09</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">3.75</td>
    <td align="right">11.18</td>
    <td align="right">9.16</td>
    <td align="center">5</td>
    <td align="right">2.2514</td>
    <td align="right">9.63</td>
    <td align="right">9.85</td>
    <td align="right">10.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4119</td>
    <td align="right">11.15</td>
    <td align="right">14.95</td>
    <td align="right">12.20</td>
    <td align="center">8</td>
    <td align="right">0.4119</td>
    <td align="right">7.45</td>
    <td align="right">12.83</td>
    <td align="right">11.16</td>
    <td align="center">8</td>
    <td align="right">0.3831</td>
    <td align="right">13.51</td>
    <td align="right">12.28</td>
    <td align="right">10.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0844</td>
    <td align="right">10.62</td>
    <td align="right">14.52</td>
    <td align="right">15.05</td>
    <td align="center">11</td>
    <td align="right">0.0844</td>
    <td align="right">9.03</td>
    <td align="right">11.39</td>
    <td align="right">11.51</td>
    <td align="center">11</td>
    <td align="right">0.0739</td>
    <td align="right">14.96</td>
    <td align="right">12.00</td>
    <td align="right">12.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0213</td>
    <td align="right">13.43</td>
    <td align="right">14.77</td>
    <td align="right">15.88</td>
    <td align="center">13</td>
    <td align="right">0.0213</td>
    <td align="right">12.55</td>
    <td align="right">13.15</td>
    <td align="right">13.66</td>
    <td align="center">14</td>
    <td align="right">0.0165</td>
    <td align="right">13.33</td>
    <td align="right">12.60</td>
    <td align="right">12.43</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">33.25</td>
    <td align="right">15.11</td>
    <td align="right">9.52</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.76</td>
    <td align="right">11.85</td>
    <td align="right">23.03</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.15</td>
    <td align="right">4.22</td>
    <td align="right">3.83</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">3.65</td>
    <td align="right">5.03</td>
    <td align="right">5.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">37.28</td>
    <td align="right">28.80</td>
    <td align="right">25.62</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">7.65</td>
    <td align="right">6.88</td>
    <td align="right">6.06</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.75</td>
    <td align="right">8.02</td>
    <td align="right">8.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">52.00</td>
    <td align="right">44.30</td>
    <td align="right">27.58</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">14.26</td>
    <td align="right">12.31</td>
    <td align="right">9.87</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.17</td>
    <td align="right">11.84</td>
    <td align="right">8.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">77.40</td>
    <td align="right">61.09</td>
    <td align="right">28.36</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">11.74</td>
    <td align="right">11.02</td>
    <td align="right">11.88</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">11.56</td>
    <td align="right">9.38</td>
    <td align="right">9.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.70</td>
    <td align="right">5.32</td>
    <td align="right">5.08</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.66</td>
    <td align="right">4.79</td>
    <td align="right">4.37</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.17</td>
    <td align="right">4.75</td>
    <td align="right">4.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">9.25</td>
    <td align="right">8.92</td>
    <td align="right">8.68</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.89</td>
    <td align="right">9.92</td>
    <td align="right">10.14</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">6.44</td>
    <td align="right">8.26</td>
    <td align="right">8.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">19.21</td>
    <td align="right">15.07</td>
    <td align="right">15.44</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">23.13</td>
    <td align="right">19.33</td>
    <td align="right">18.64</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">16.93</td>
    <td align="right">14.97</td>
    <td align="right">12.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">26.19</td>
    <td align="right">23.63</td>
    <td align="right">25.73</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">28.55</td>
    <td align="right">28.30</td>
    <td align="right">26.92</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">20.51</td>
    <td align="right">22.28</td>
    <td align="right">14.09</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">6.67</td>
    <td align="right">8.03</td>
    <td align="right">7.58</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.65</td>
    <td align="right">9.17</td>
    <td align="right">5.79</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.93</td>
    <td align="right">9.22</td>
    <td align="right">6.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">11.19</td>
    <td align="right">10.87</td>
    <td align="right">10.41</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.13</td>
    <td align="right">13.25</td>
    <td align="right">13.44</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.84</td>
    <td align="right">15.43</td>
    <td align="right">11.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">21.67</td>
    <td align="right">23.00</td>
    <td align="right">11.88</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">19.42</td>
    <td align="right">20.54</td>
    <td align="right">22.18</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">25.70</td>
    <td align="right">20.00</td>
    <td align="right">21.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">19.08</td>
    <td align="right">16.32</td>
    <td align="right">9.73</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">22.71</td>
    <td align="right">26.88</td>
    <td align="right">25.49</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">36.49</td>
    <td align="right">36.46</td>
    <td align="right">33.19</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">21.57</td>
    <td align="right">25.01</td>
    <td align="right">24.71</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">22.44</td>
    <td align="right">21.74</td>
    <td align="right">24.46</td>
    <td align="center">5</td>
    <td align="right">2.2818</td>
    <td align="right">25.05</td>
    <td align="right">22.26</td>
    <td align="right">17.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4140</td>
    <td align="right">23.16</td>
    <td align="right">22.74</td>
    <td align="right">22.54</td>
    <td align="center">8</td>
    <td align="right">0.4140</td>
    <td align="right">31.67</td>
    <td align="right">31.30</td>
    <td align="right">33.74</td>
    <td align="center">8</td>
    <td align="right">0.3795</td>
    <td align="right">51.10</td>
    <td align="right">27.26</td>
    <td align="right">22.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0895</td>
    <td align="right">31.66</td>
    <td align="right">34.34</td>
    <td align="right">39.06</td>
    <td align="center">11</td>
    <td align="right">0.0895</td>
    <td align="right">38.38</td>
    <td align="right">29.15</td>
    <td align="right">27.29</td>
    <td align="center">11</td>
    <td align="right">0.0721</td>
    <td align="right">46.64</td>
    <td align="right">35.02</td>
    <td align="right">35.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0212</td>
    <td align="right">47.09</td>
    <td align="right">42.46</td>
    <td align="right">35.73</td>
    <td align="center">13</td>
    <td align="right">0.0212</td>
    <td align="right">37.81</td>
    <td align="right">33.82</td>
    <td align="right">26.79</td>
    <td align="center">14</td>
    <td align="right">0.0165</td>
    <td align="right">50.37</td>
    <td align="right">35.15</td>
    <td align="right">34.17</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">35.28</td>
    <td align="right">5.95</td>
    <td align="right">3.75</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.20</td>
    <td align="right">12.57</td>
    <td align="right">17.03</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.85</td>
    <td align="right">4.27</td>
    <td align="right">4.26</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">7.00</td>
    <td align="right">5.24</td>
    <td align="right">5.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">19.06</td>
    <td align="right">17.85</td>
    <td align="right">17.65</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.97</td>
    <td align="right">4.73</td>
    <td align="right">4.82</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.08</td>
    <td align="right">5.98</td>
    <td align="right">6.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.78</td>
    <td align="right">21.33</td>
    <td align="right">16.67</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.63</td>
    <td align="right">5.37</td>
    <td align="right">5.36</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.36</td>
    <td align="right">6.61</td>
    <td align="right">6.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.32</td>
    <td align="right">27.49</td>
    <td align="right">17.32</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.97</td>
    <td align="right">6.21</td>
    <td align="right">6.01</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.44</td>
    <td align="right">7.45</td>
    <td align="right">7.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.84</td>
    <td align="right">5.54</td>
    <td align="right">5.50</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">11.71</td>
    <td align="right">5.58</td>
    <td align="right">5.59</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.39</td>
    <td align="right">3.96</td>
    <td align="right">3.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.09</td>
    <td align="right">8.70</td>
    <td align="right">8.14</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.26</td>
    <td align="right">8.71</td>
    <td align="right">8.73</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.95</td>
    <td align="right">4.89</td>
    <td align="right">4.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.38</td>
    <td align="right">10.79</td>
    <td align="right">10.88</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.07</td>
    <td align="right">10.51</td>
    <td align="right">10.59</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.03</td>
    <td align="right">7.15</td>
    <td align="right">5.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">17.44</td>
    <td align="right">14.24</td>
    <td align="right">14.36</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">19.06</td>
    <td align="right">13.82</td>
    <td align="right">12.81</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.12</td>
    <td align="right">7.29</td>
    <td align="right">5.44</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.27</td>
    <td align="right">3.89</td>
    <td align="right">3.87</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.53</td>
    <td align="right">5.42</td>
    <td align="right">5.39</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.73</td>
    <td align="right">5.39</td>
    <td align="right">5.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.35</td>
    <td align="right">5.65</td>
    <td align="right">4.71</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.78</td>
    <td align="right">5.90</td>
    <td align="right">5.10</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.97</td>
    <td align="right">7.10</td>
    <td align="right">6.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.11</td>
    <td align="right">6.82</td>
    <td align="right">5.06</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.90</td>
    <td align="right">9.27</td>
    <td align="right">7.53</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">10.18</td>
    <td align="right">9.37</td>
    <td align="right">7.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.21</td>
    <td align="right">6.91</td>
    <td align="right">5.10</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.11</td>
    <td align="right">10.60</td>
    <td align="right">7.60</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.35</td>
    <td align="right">10.47</td>
    <td align="right">7.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">8.70</td>
    <td align="right">17.06</td>
    <td align="right">17.06</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">9.06</td>
    <td align="right">23.98</td>
    <td align="right">23.91</td>
    <td align="center">5</td>
    <td align="right">2.2514</td>
    <td align="right">11.19</td>
    <td align="right">24.72</td>
    <td align="right">24.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4119</td>
    <td align="right">12.61</td>
    <td align="right">17.90</td>
    <td align="right">17.89</td>
    <td align="center">8</td>
    <td align="right">0.4119</td>
    <td align="right">13.26</td>
    <td align="right">21.69</td>
    <td align="right">21.60</td>
    <td align="center">8</td>
    <td align="right">0.3831</td>
    <td align="right">15.72</td>
    <td align="right">25.95</td>
    <td align="right">25.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0844</td>
    <td align="right">16.58</td>
    <td align="right">19.06</td>
    <td align="right">19.08</td>
    <td align="center">11</td>
    <td align="right">0.0844</td>
    <td align="right">17.26</td>
    <td align="right">23.18</td>
    <td align="right">23.18</td>
    <td align="center">11</td>
    <td align="right">0.0739</td>
    <td align="right">19.64</td>
    <td align="right">28.23</td>
    <td align="right">28.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0213</td>
    <td align="right">19.31</td>
    <td align="right">20.36</td>
    <td align="right">20.41</td>
    <td align="center">13</td>
    <td align="right">0.0213</td>
    <td align="right">20.20</td>
    <td align="right">23.89</td>
    <td align="right">23.74</td>
    <td align="center">14</td>
    <td align="right">0.0165</td>
    <td align="right">23.17</td>
    <td align="right">31.71</td>
    <td align="right">31.44</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">48.68</td>
    <td align="right">24.45</td>
    <td align="right">9.67</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.73</td>
    <td align="right">13.25</td>
    <td align="right">17.80</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.20</td>
    <td align="right">4.54</td>
    <td align="right">4.52</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">8.13</td>
    <td align="right">5.74</td>
    <td align="right">5.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">24.81</td>
    <td align="right">18.96</td>
    <td align="right">18.48</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.04</td>
    <td align="right">6.57</td>
    <td align="right">7.32</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.71</td>
    <td align="right">6.42</td>
    <td align="right">6.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">30.49</td>
    <td align="right">30.39</td>
    <td align="right">18.49</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">11.05</td>
    <td align="right">6.76</td>
    <td align="right">6.27</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">12.64</td>
    <td align="right">8.11</td>
    <td align="right">12.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">76.23</td>
    <td align="right">56.07</td>
    <td align="right">21.06</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">16.71</td>
    <td align="right">16.23</td>
    <td align="right">11.36</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">17.71</td>
    <td align="right">14.25</td>
    <td align="right">14.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.25</td>
    <td align="right">6.25</td>
    <td align="right">6.28</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.51</td>
    <td align="right">6.40</td>
    <td align="right">6.35</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.81</td>
    <td align="right">4.16</td>
    <td align="right">4.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">15.96</td>
    <td align="right">10.55</td>
    <td align="right">10.54</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">18.31</td>
    <td align="right">9.29</td>
    <td align="right">9.32</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.48</td>
    <td align="right">5.93</td>
    <td align="right">4.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">19.80</td>
    <td align="right">13.64</td>
    <td align="right">14.35</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">19.77</td>
    <td align="right">15.89</td>
    <td align="right">16.99</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.20</td>
    <td align="right">19.57</td>
    <td align="right">13.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">25.30</td>
    <td align="right">21.05</td>
    <td align="right">21.04</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">32.31</td>
    <td align="right">23.75</td>
    <td align="right">27.10</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">16.02</td>
    <td align="right">16.00</td>
    <td align="right">12.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.70</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.97</td>
    <td align="right">5.88</td>
    <td align="right">5.87</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.11</td>
    <td align="right">5.76</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.87</td>
    <td align="right">6.35</td>
    <td align="right">5.27</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.60</td>
    <td align="right">7.44</td>
    <td align="right">6.21</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.86</td>
    <td align="right">8.12</td>
    <td align="right">6.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">9.55</td>
    <td align="right">12.41</td>
    <td align="right">6.66</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">12.23</td>
    <td align="right">11.20</td>
    <td align="right">9.27</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">12.51</td>
    <td align="right">10.63</td>
    <td align="right">9.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">18.16</td>
    <td align="right">19.24</td>
    <td align="right">14.32</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">18.55</td>
    <td align="right">22.11</td>
    <td align="right">15.99</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">21.02</td>
    <td align="right">26.27</td>
    <td align="right">16.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">10.01</td>
    <td align="right">16.45</td>
    <td align="right">16.60</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">10.30</td>
    <td align="right">25.09</td>
    <td align="right">24.95</td>
    <td align="center">5</td>
    <td align="right">2.2818</td>
    <td align="right">11.86</td>
    <td align="right">26.62</td>
    <td align="right">26.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4140</td>
    <td align="right">20.10</td>
    <td align="right">20.50</td>
    <td align="right">21.15</td>
    <td align="center">8</td>
    <td align="right">0.4140</td>
    <td align="right">19.05</td>
    <td align="right">27.43</td>
    <td align="right">27.15</td>
    <td align="center">8</td>
    <td align="right">0.3795</td>
    <td align="right">26.20</td>
    <td align="right">40.78</td>
    <td align="right">39.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0895</td>
    <td align="right">30.90</td>
    <td align="right">32.80</td>
    <td align="right">32.28</td>
    <td align="center">11</td>
    <td align="right">0.0895</td>
    <td align="right">35.85</td>
    <td align="right">41.12</td>
    <td align="right">42.09</td>
    <td align="center">11</td>
    <td align="right">0.0721</td>
    <td align="right">45.16</td>
    <td align="right">56.17</td>
    <td align="right">56.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0212</td>
    <td align="right">47.24</td>
    <td align="right">44.50</td>
    <td align="right">39.48</td>
    <td align="center">13</td>
    <td align="right">0.0212</td>
    <td align="right">45.19</td>
    <td align="right">55.24</td>
    <td align="right">53.20</td>
    <td align="center">14</td>
    <td align="right">0.0165</td>
    <td align="right">51.70</td>
    <td align="right">75.95</td>
    <td align="right">78.84</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">63.24</td>
    <td align="right">34.86</td>
    <td align="right">18.27</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.64</td>
    <td align="right">42.47</td>
    <td align="right">36.59</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.51</td>
    <td align="right">15.64</td>
    <td align="right">15.51</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.16</td>
    <td align="right">19.21</td>
    <td align="right">19.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.67</td>
    <td align="right">64.05</td>
    <td align="right">39.31</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.35</td>
    <td align="right">19.64</td>
    <td align="right">19.71</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.17</td>
    <td align="right">18.67</td>
    <td align="right">18.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">45.53</td>
    <td align="right">78.44</td>
    <td align="right">38.37</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.46</td>
    <td align="right">18.63</td>
    <td align="right">18.54</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.18</td>
    <td align="right">18.36</td>
    <td align="right">18.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">54.10</td>
    <td align="right">90.86</td>
    <td align="right">35.68</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">17.37</td>
    <td align="right">18.63</td>
    <td align="right">18.66</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.18</td>
    <td align="right">19.74</td>
    <td align="right">19.61</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.21</td>
    <td align="right">21.31</td>
    <td align="right">21.29</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.67</td>
    <td align="right">22.22</td>
    <td align="right">22.26</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.97</td>
    <td align="right">13.65</td>
    <td align="right">13.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.37</td>
    <td align="right">26.02</td>
    <td align="right">26.00</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.74</td>
    <td align="right">27.70</td>
    <td align="right">27.67</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.95</td>
    <td align="right">15.83</td>
    <td align="right">15.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.27</td>
    <td align="right">33.03</td>
    <td align="right">33.12</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.67</td>
    <td align="right">46.56</td>
    <td align="right">46.63</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">15.04</td>
    <td align="right">19.59</td>
    <td align="right">19.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">33.40</td>
    <td align="right">34.06</td>
    <td align="right">34.16</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">76.23</td>
    <td align="right">55.21</td>
    <td align="right">55.35</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">22.41</td>
    <td align="right">23.87</td>
    <td align="right">23.85</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">15.47</td>
    <td align="right">15.59</td>
    <td align="right">15.58</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.25</td>
    <td align="right">21.24</td>
    <td align="right">21.28</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.69</td>
    <td align="right">22.23</td>
    <td align="right">22.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">20.13</td>
    <td align="right">20.54</td>
    <td align="right">20.54</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.34</td>
    <td align="right">25.99</td>
    <td align="right">26.01</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.65</td>
    <td align="right">27.66</td>
    <td align="right">27.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.35</td>
    <td align="right">24.78</td>
    <td align="right">24.79</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.28</td>
    <td align="right">33.07</td>
    <td align="right">33.07</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.87</td>
    <td align="right">46.73</td>
    <td align="right">46.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">33.37</td>
    <td align="right">35.25</td>
    <td align="right">35.20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">33.16</td>
    <td align="right">33.96</td>
    <td align="right">34.01</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">76.28</td>
    <td align="right">55.24</td>
    <td align="right">55.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">12.87</td>
    <td align="right">31.67</td>
    <td align="right">31.63</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">17.12</td>
    <td align="right">28.40</td>
    <td align="right">28.42</td>
    <td align="center">5</td>
    <td align="right">2.2606</td>
    <td align="right">30.18</td>
    <td align="right">47.41</td>
    <td align="right">47.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4116</td>
    <td align="right">22.16</td>
    <td align="right">38.79</td>
    <td align="right">42.61</td>
    <td align="center">8</td>
    <td align="right">0.4116</td>
    <td align="right">30.81</td>
    <td align="right">40.12</td>
    <td align="right">40.24</td>
    <td align="center">8</td>
    <td align="right">0.3726</td>
    <td align="right">40.80</td>
    <td align="right">62.16</td>
    <td align="right">61.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0903</td>
    <td align="right">26.63</td>
    <td align="right">47.37</td>
    <td align="right">47.22</td>
    <td align="center">11</td>
    <td align="right">0.0903</td>
    <td align="right">36.20</td>
    <td align="right">46.37</td>
    <td align="right">46.72</td>
    <td align="center">11</td>
    <td align="right">0.0739</td>
    <td align="right">49.70</td>
    <td align="right">63.65</td>
    <td align="right">71.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0200</td>
    <td align="right">34.66</td>
    <td align="right">53.94</td>
    <td align="right">53.68</td>
    <td align="center">13</td>
    <td align="right">0.0200</td>
    <td align="right">44.68</td>
    <td align="right">59.81</td>
    <td align="right">59.36</td>
    <td align="center">14</td>
    <td align="right">0.0174</td>
    <td align="right">62.03</td>
    <td align="right">81.11</td>
    <td align="right">86.61</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">90.76</td>
    <td align="right">115.15</td>
    <td align="right">27.72</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">30.27</td>
    <td align="right">48.41</td>
    <td align="right">44.16</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">15.01</td>
    <td align="right">17.59</td>
    <td align="right">20.27</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">25.66</td>
    <td align="right">29.95</td>
    <td align="right">26.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">50.94</td>
    <td align="right">84.15</td>
    <td align="right">50.42</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">27.28</td>
    <td align="right">32.53</td>
    <td align="right">33.74</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">37.95</td>
    <td align="right">38.63</td>
    <td align="right">34.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">131.82</td>
    <td align="right">194.14</td>
    <td align="right">71.00</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">40.72</td>
    <td align="right">39.52</td>
    <td align="right">39.60</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">45.46</td>
    <td align="right">46.39</td>
    <td align="right">47.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">230.53</td>
    <td align="right">351.95</td>
    <td align="right">101.05</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">49.77</td>
    <td align="right">48.99</td>
    <td align="right">48.78</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">51.75</td>
    <td align="right">54.05</td>
    <td align="right">52.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">18.64</td>
    <td align="right">25.30</td>
    <td align="right">23.95</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">67.02</td>
    <td align="right">35.93</td>
    <td align="right">27.57</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">12.90</td>
    <td align="right">15.06</td>
    <td align="right">14.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">22.88</td>
    <td align="right">26.08</td>
    <td align="right">26.87</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">41.72</td>
    <td align="right">28.64</td>
    <td align="right">28.43</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.76</td>
    <td align="right">15.68</td>
    <td align="right">15.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">39.50</td>
    <td align="right">33.48</td>
    <td align="right">33.44</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">65.03</td>
    <td align="right">47.62</td>
    <td align="right">49.56</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">14.68</td>
    <td align="right">20.31</td>
    <td align="right">31.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">45.51</td>
    <td align="right">52.15</td>
    <td align="right">38.53</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">85.40</td>
    <td align="right">69.32</td>
    <td align="right">65.49</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">31.18</td>
    <td align="right">26.85</td>
    <td align="right">25.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">15.77</td>
    <td align="right">15.92</td>
    <td align="right">15.93</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.44</td>
    <td align="right">21.60</td>
    <td align="right">21.64</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">32.72</td>
    <td align="right">22.84</td>
    <td align="right">22.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">19.60</td>
    <td align="right">20.05</td>
    <td align="right">20.05</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.31</td>
    <td align="right">25.32</td>
    <td align="right">25.36</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.25</td>
    <td align="right">27.94</td>
    <td align="right">28.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">27.34</td>
    <td align="right">23.83</td>
    <td align="right">23.93</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.79</td>
    <td align="right">33.31</td>
    <td align="right">33.28</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">64.93</td>
    <td align="right">47.59</td>
    <td align="right">47.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">36.75</td>
    <td align="right">38.96</td>
    <td align="right">38.63</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">34.59</td>
    <td align="right">36.14</td>
    <td align="right">37.44</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">78.83</td>
    <td align="right">57.51</td>
    <td align="right">57.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">12.89</td>
    <td align="right">31.60</td>
    <td align="right">31.59</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">17.36</td>
    <td align="right">28.46</td>
    <td align="right">28.49</td>
    <td align="center">5</td>
    <td align="right">2.2853</td>
    <td align="right">30.76</td>
    <td align="right">49.64</td>
    <td align="right">49.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4167</td>
    <td align="right">22.17</td>
    <td align="right">38.81</td>
    <td align="right">42.93</td>
    <td align="center">8</td>
    <td align="right">0.4167</td>
    <td align="right">30.42</td>
    <td align="right">39.22</td>
    <td align="right">39.24</td>
    <td align="center">8</td>
    <td align="right">0.3806</td>
    <td align="right">40.51</td>
    <td align="right">62.57</td>
    <td align="right">62.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0874</td>
    <td align="right">25.83</td>
    <td align="right">46.25</td>
    <td align="right">46.38</td>
    <td align="center">11</td>
    <td align="right">0.0874</td>
    <td align="right">35.03</td>
    <td align="right">48.99</td>
    <td align="right">46.23</td>
    <td align="center">11</td>
    <td align="right">0.0728</td>
    <td align="right">50.45</td>
    <td align="right">63.08</td>
    <td align="right">81.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0207</td>
    <td align="right">40.09</td>
    <td align="right">65.42</td>
    <td align="right">64.51</td>
    <td align="center">13</td>
    <td align="right">0.0207</td>
    <td align="right">47.34</td>
    <td align="right">68.52</td>
    <td align="right">69.38</td>
    <td align="center">14</td>
    <td align="right">0.0169</td>
    <td align="right">89.64</td>
    <td align="right">102.45</td>
    <td align="right">102.57</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">60.69</td>
    <td align="right">10.32</td>
    <td align="right">7.32</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">13.82</td>
    <td align="right">22.70</td>
    <td align="right">26.52</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.48</td>
    <td align="right">12.27</td>
    <td align="right">12.30</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.68</td>
    <td align="right">13.80</td>
    <td align="right">13.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.73</td>
    <td align="right">35.27</td>
    <td align="right">28.74</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">11.94</td>
    <td align="right">14.12</td>
    <td align="right">14.16</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.64</td>
    <td align="right">15.34</td>
    <td align="right">15.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.33</td>
    <td align="right">47.28</td>
    <td align="right">30.14</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.81</td>
    <td align="right">15.35</td>
    <td align="right">15.26</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.55</td>
    <td align="right">16.67</td>
    <td align="right">16.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">29.55</td>
    <td align="right">59.84</td>
    <td align="right">29.17</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">13.97</td>
    <td align="right">15.33</td>
    <td align="right">15.40</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.09</td>
    <td align="right">16.97</td>
    <td align="right">16.91</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.77</td>
    <td align="right">16.02</td>
    <td align="right">16.00</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.25</td>
    <td align="right">16.65</td>
    <td align="right">16.65</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.10</td>
    <td align="right">9.33</td>
    <td align="right">9.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.31</td>
    <td align="right">22.47</td>
    <td align="right">22.61</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.29</td>
    <td align="right">22.27</td>
    <td align="right">22.28</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.73</td>
    <td align="right">13.92</td>
    <td align="right">13.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.28</td>
    <td align="right">32.33</td>
    <td align="right">32.54</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">26.30</td>
    <td align="right">30.71</td>
    <td align="right">30.73</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.44</td>
    <td align="right">17.59</td>
    <td align="right">17.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.20</td>
    <td align="right">34.25</td>
    <td align="right">33.89</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">31.81</td>
    <td align="right">33.66</td>
    <td align="right">33.68</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">15.52</td>
    <td align="right">18.79</td>
    <td align="right">18.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">6.61</td>
    <td align="right">9.42</td>
    <td align="right">9.44</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.72</td>
    <td align="right">16.20</td>
    <td align="right">16.19</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.25</td>
    <td align="right">16.74</td>
    <td align="right">16.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">10.78</td>
    <td align="right">13.79</td>
    <td align="right">13.70</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.33</td>
    <td align="right">22.46</td>
    <td align="right">22.49</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.32</td>
    <td align="right">22.36</td>
    <td align="right">22.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.49</td>
    <td align="right">17.55</td>
    <td align="right">17.57</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.98</td>
    <td align="right">31.99</td>
    <td align="right">32.01</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.58</td>
    <td align="right">30.53</td>
    <td align="right">30.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">15.17</td>
    <td align="right">19.21</td>
    <td align="right">19.17</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">25.69</td>
    <td align="right">33.56</td>
    <td align="right">33.54</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">31.98</td>
    <td align="right">33.63</td>
    <td align="right">33.70</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">10.52</td>
    <td align="right">32.18</td>
    <td align="right">31.84</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">13.70</td>
    <td align="right">27.87</td>
    <td align="right">28.14</td>
    <td align="center">5</td>
    <td align="right">2.2606</td>
    <td align="right">48.03</td>
    <td align="right">36.15</td>
    <td align="right">35.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4116</td>
    <td align="right">16.54</td>
    <td align="right">33.39</td>
    <td align="right">33.43</td>
    <td align="center">8</td>
    <td align="right">0.4116</td>
    <td align="right">21.65</td>
    <td align="right">39.69</td>
    <td align="right">39.71</td>
    <td align="center">8</td>
    <td align="right">0.3726</td>
    <td align="right">55.17</td>
    <td align="right">53.64</td>
    <td align="right">53.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0903</td>
    <td align="right">19.40</td>
    <td align="right">35.07</td>
    <td align="right">35.09</td>
    <td align="center">11</td>
    <td align="right">0.0903</td>
    <td align="right">28.00</td>
    <td align="right">41.68</td>
    <td align="right">41.71</td>
    <td align="center">11</td>
    <td align="right">0.0739</td>
    <td align="right">63.81</td>
    <td align="right">54.23</td>
    <td align="right">54.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0200</td>
    <td align="right">22.63</td>
    <td align="right">37.08</td>
    <td align="right">37.09</td>
    <td align="center">13</td>
    <td align="right">0.0200</td>
    <td align="right">32.75</td>
    <td align="right">48.65</td>
    <td align="right">47.28</td>
    <td align="center">14</td>
    <td align="right">0.0174</td>
    <td align="right">71.12</td>
    <td align="right">66.94</td>
    <td align="right">66.90</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">77.11</td>
    <td align="right">45.61</td>
    <td align="right">10.69</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">14.14</td>
    <td align="right">22.75</td>
    <td align="right">28.14</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.67</td>
    <td align="right">12.48</td>
    <td align="right">12.46</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">11.84</td>
    <td align="right">13.92</td>
    <td align="right">13.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.53</td>
    <td align="right">34.87</td>
    <td align="right">29.43</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">12.42</td>
    <td align="right">14.94</td>
    <td align="right">15.16</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">15.33</td>
    <td align="right">17.44</td>
    <td align="right">16.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">26.12</td>
    <td align="right">69.67</td>
    <td align="right">36.66</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">14.53</td>
    <td align="right">17.99</td>
    <td align="right">17.14</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">14.97</td>
    <td align="right">17.11</td>
    <td align="right">17.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">38.62</td>
    <td align="right">76.81</td>
    <td align="right">33.41</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">18.46</td>
    <td align="right">20.85</td>
    <td align="right">33.53</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">25.41</td>
    <td align="right">33.16</td>
    <td align="right">24.77</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.25</td>
    <td align="right">16.60</td>
    <td align="right">16.61</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.30</td>
    <td align="right">17.40</td>
    <td align="right">17.41</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.24</td>
    <td align="right">9.41</td>
    <td align="right">9.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.01</td>
    <td align="right">22.13</td>
    <td align="right">22.12</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.43</td>
    <td align="right">22.18</td>
    <td align="right">22.27</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.11</td>
    <td align="right">13.97</td>
    <td align="right">14.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.89</td>
    <td align="right">34.58</td>
    <td align="right">33.43</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">26.24</td>
    <td align="right">32.26</td>
    <td align="right">31.65</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">15.67</td>
    <td align="right">19.70</td>
    <td align="right">16.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">36.11</td>
    <td align="right">41.88</td>
    <td align="right">42.31</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">36.40</td>
    <td align="right">42.52</td>
    <td align="right">43.31</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">18.84</td>
    <td align="right">24.52</td>
    <td align="right">29.62</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">6.68</td>
    <td align="right">9.50</td>
    <td align="right">9.49</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.28</td>
    <td align="right">16.59</td>
    <td align="right">16.61</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.31</td>
    <td align="right">17.39</td>
    <td align="right">17.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">11.94</td>
    <td align="right">16.97</td>
    <td align="right">13.46</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.13</td>
    <td align="right">22.37</td>
    <td align="right">22.08</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.51</td>
    <td align="right">22.39</td>
    <td align="right">22.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">13.14</td>
    <td align="right">17.54</td>
    <td align="right">17.73</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">26.07</td>
    <td align="right">34.45</td>
    <td align="right">34.91</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">26.34</td>
    <td align="right">31.51</td>
    <td align="right">31.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">20.32</td>
    <td align="right">25.68</td>
    <td align="right">25.83</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">31.68</td>
    <td align="right">42.95</td>
    <td align="right">45.06</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">45.55</td>
    <td align="right">43.44</td>
    <td align="right">51.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">11.57</td>
    <td align="right">30.01</td>
    <td align="right">29.22</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">14.04</td>
    <td align="right">27.93</td>
    <td align="right">30.27</td>
    <td align="center">5</td>
    <td align="right">2.2853</td>
    <td align="right">47.33</td>
    <td align="right">38.39</td>
    <td align="right">38.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4167</td>
    <td align="right">18.08</td>
    <td align="right">32.79</td>
    <td align="right">32.37</td>
    <td align="center">8</td>
    <td align="right">0.4167</td>
    <td align="right">22.07</td>
    <td align="right">44.68</td>
    <td align="right">40.61</td>
    <td align="center">8</td>
    <td align="right">0.3806</td>
    <td align="right">56.88</td>
    <td align="right">57.65</td>
    <td align="right">54.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0874</td>
    <td align="right">20.16</td>
    <td align="right">36.51</td>
    <td align="right">41.06</td>
    <td align="center">11</td>
    <td align="right">0.0874</td>
    <td align="right">38.41</td>
    <td align="right">48.84</td>
    <td align="right">41.76</td>
    <td align="center">11</td>
    <td align="right">0.0728</td>
    <td align="right">72.58</td>
    <td align="right">59.37</td>
    <td align="right">78.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0207</td>
    <td align="right">27.13</td>
    <td align="right">45.78</td>
    <td align="right">45.14</td>
    <td align="center">13</td>
    <td align="right">0.0207</td>
    <td align="right">41.81</td>
    <td align="right">60.13</td>
    <td align="right">68.13</td>
    <td align="center">14</td>
    <td align="right">0.0169</td>
    <td align="right">86.18</td>
    <td align="right">87.41</td>
    <td align="right">86.58</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">42.03</td>
    <td align="right">8.54</td>
    <td align="right">6.63</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">59.33</td>
    <td align="right">58.58</td>
    <td align="right">44.48</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.72</td>
    <td align="right">23.31</td>
    <td align="right">26.40</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">25.00</td>
    <td align="right">26.16</td>
    <td align="right">29.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">89.61</td>
    <td align="right">84.73</td>
    <td align="right">46.62</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">24.00</td>
    <td align="right">24.30</td>
    <td align="right">26.28</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">27.23</td>
    <td align="right">28.49</td>
    <td align="right">30.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">110.16</td>
    <td align="right">101.80</td>
    <td align="right">46.38</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.29</td>
    <td align="right">25.32</td>
    <td align="right">26.45</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.42</td>
    <td align="right">30.81</td>
    <td align="right">31.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">139.73</td>
    <td align="right">127.40</td>
    <td align="right">47.15</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.31</td>
    <td align="right">26.98</td>
    <td align="right">27.92</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">31.22</td>
    <td align="right">33.56</td>
    <td align="right">33.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">23.59</td>
    <td align="right">43.20</td>
    <td align="right">43.05</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">27.28</td>
    <td align="right">43.60</td>
    <td align="right">43.44</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.55</td>
    <td align="right">24.86</td>
    <td align="right">24.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.18</td>
    <td align="right">58.55</td>
    <td align="right">58.86</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.40</td>
    <td align="right">59.68</td>
    <td align="right">59.66</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.58</td>
    <td align="right">36.48</td>
    <td align="right">25.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.07</td>
    <td align="right">80.28</td>
    <td align="right">80.53</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">45.89</td>
    <td align="right">81.03</td>
    <td align="right">80.72</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">29.04</td>
    <td align="right">54.71</td>
    <td align="right">39.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">44.16</td>
    <td align="right">88.74</td>
    <td align="right">88.67</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">52.31</td>
    <td align="right">95.83</td>
    <td align="right">95.84</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.33</td>
    <td align="right">55.34</td>
    <td align="right">40.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">18.67</td>
    <td align="right">26.03</td>
    <td align="right">26.00</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.64</td>
    <td align="right">28.80</td>
    <td align="right">29.08</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.89</td>
    <td align="right">30.58</td>
    <td align="right">30.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">18.93</td>
    <td align="right">46.83</td>
    <td align="right">35.00</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.44</td>
    <td align="right">40.63</td>
    <td align="right">27.64</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">21.04</td>
    <td align="right">51.72</td>
    <td align="right">40.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.72</td>
    <td align="right">54.55</td>
    <td align="right">39.16</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">33.00</td>
    <td align="right">53.08</td>
    <td align="right">34.78</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.25</td>
    <td align="right">60.76</td>
    <td align="right">44.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.84</td>
    <td align="right">55.07</td>
    <td align="right">39.49</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.84</td>
    <td align="right">64.05</td>
    <td align="right">43.94</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.31</td>
    <td align="right">64.14</td>
    <td align="right">44.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">23.41</td>
    <td align="right">26.80</td>
    <td align="right">26.93</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">25.32</td>
    <td align="right">32.50</td>
    <td align="right">53.65</td>
    <td align="center">5</td>
    <td align="right">2.2606</td>
    <td align="right">30.07</td>
    <td align="right">40.84</td>
    <td align="right">59.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4116</td>
    <td align="right">35.01</td>
    <td align="right">37.61</td>
    <td align="right">37.65</td>
    <td align="center">8</td>
    <td align="right">0.4116</td>
    <td align="right">38.17</td>
    <td align="right">43.47</td>
    <td align="right">72.58</td>
    <td align="center">8</td>
    <td align="right">0.3726</td>
    <td align="right">43.83</td>
    <td align="right">55.79</td>
    <td align="right">82.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0903</td>
    <td align="right">40.53</td>
    <td align="right">41.00</td>
    <td align="right">41.35</td>
    <td align="center">11</td>
    <td align="right">0.0903</td>
    <td align="right">45.25</td>
    <td align="right">48.21</td>
    <td align="right">81.73</td>
    <td align="center">11</td>
    <td align="right">0.0739</td>
    <td align="right">50.80</td>
    <td align="right">62.34</td>
    <td align="right">92.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0200</td>
    <td align="right">47.96</td>
    <td align="right">49.51</td>
    <td align="right">49.80</td>
    <td align="center">13</td>
    <td align="right">0.0200</td>
    <td align="right">54.03</td>
    <td align="right">60.93</td>
    <td align="right">101.50</td>
    <td align="center">14</td>
    <td align="right">0.0174</td>
    <td align="right">61.73</td>
    <td align="right">75.37</td>
    <td align="right">115.11</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.53</td>
    <td align="right">36.09</td>
    <td align="right">11.00</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">67.35</td>
    <td align="right">63.91</td>
    <td align="right">48.46</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">23.44</td>
    <td align="right">23.62</td>
    <td align="right">27.99</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">27.62</td>
    <td align="right">29.15</td>
    <td align="right">33.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">97.67</td>
    <td align="right">89.89</td>
    <td align="right">49.94</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">25.63</td>
    <td align="right">24.76</td>
    <td align="right">27.30</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">29.70</td>
    <td align="right">30.68</td>
    <td align="right">33.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">122.79</td>
    <td align="right">110.37</td>
    <td align="right">49.41</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">27.57</td>
    <td align="right">26.29</td>
    <td align="right">27.68</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">32.87</td>
    <td align="right">34.04</td>
    <td align="right">44.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">171.41</td>
    <td align="right">147.20</td>
    <td align="right">53.86</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">32.14</td>
    <td align="right">30.51</td>
    <td align="right">31.36</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">46.81</td>
    <td align="right">53.43</td>
    <td align="right">54.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">25.51</td>
    <td align="right">43.74</td>
    <td align="right">43.75</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">29.88</td>
    <td align="right">44.33</td>
    <td align="right">44.40</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">20.07</td>
    <td align="right">29.50</td>
    <td align="right">29.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">30.27</td>
    <td align="right">59.20</td>
    <td align="right">59.56</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">37.02</td>
    <td align="right">60.55</td>
    <td align="right">60.30</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">18.97</td>
    <td align="right">40.30</td>
    <td align="right">29.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">43.17</td>
    <td align="right">81.24</td>
    <td align="right">82.04</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">49.90</td>
    <td align="right">82.82</td>
    <td align="right">82.69</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">32.21</td>
    <td align="right">61.86</td>
    <td align="right">45.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">48.83</td>
    <td align="right">92.39</td>
    <td align="right">92.25</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">58.94</td>
    <td align="right">101.51</td>
    <td align="right">101.09</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">36.75</td>
    <td align="right">68.07</td>
    <td align="right">52.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">19.85</td>
    <td align="right">31.00</td>
    <td align="right">31.09</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">21.73</td>
    <td align="right">33.43</td>
    <td align="right">33.36</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">22.54</td>
    <td align="right">36.96</td>
    <td align="right">35.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">19.99</td>
    <td align="right">51.44</td>
    <td align="right">39.62</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">19.32</td>
    <td align="right">42.20</td>
    <td align="right">30.35</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">22.07</td>
    <td align="right">56.16</td>
    <td align="right">44.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">30.92</td>
    <td align="right">59.39</td>
    <td align="right">43.93</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">34.67</td>
    <td align="right">57.33</td>
    <td align="right">38.73</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">34.02</td>
    <td align="right">66.01</td>
    <td align="right">48.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">36.35</td>
    <td align="right">68.81</td>
    <td align="right">51.67</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">36.51</td>
    <td align="right">70.72</td>
    <td align="right">49.53</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">37.37</td>
    <td align="right">74.19</td>
    <td align="right">53.92</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint32_t[16],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">26.01</td>
    <td align="right">27.78</td>
    <td align="right">27.90</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">27.76</td>
    <td align="right">33.37</td>
    <td align="right">57.41</td>
    <td align="center">5</td>
    <td align="right">2.2853</td>
    <td align="right">34.28</td>
    <td align="right">44.82</td>
    <td align="right">63.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4167</td>
    <td align="right">38.51</td>
    <td align="right">38.47</td>
    <td align="right">38.41</td>
    <td align="center">8</td>
    <td align="right">0.4167</td>
    <td align="right">45.48</td>
    <td align="right">44.91</td>
    <td align="right">76.72</td>
    <td align="center">8</td>
    <td align="right">0.3806</td>
    <td align="right">47.95</td>
    <td align="right">59.53</td>
    <td align="right">86.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0874</td>
    <td align="right">45.03</td>
    <td align="right">42.00</td>
    <td align="right">42.51</td>
    <td align="center">11</td>
    <td align="right">0.0874</td>
    <td align="right">50.13</td>
    <td align="right">50.48</td>
    <td align="right">83.82</td>
    <td align="center">11</td>
    <td align="right">0.0728</td>
    <td align="right">56.38</td>
    <td align="right">68.25</td>
    <td align="right">115.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0207</td>
    <td align="right">55.71</td>
    <td align="right">53.73</td>
    <td align="right">54.10</td>
    <td align="center">13</td>
    <td align="right">0.0207</td>
    <td align="right">80.94</td>
    <td align="right">74.40</td>
    <td align="right">106.45</td>
    <td align="center">14</td>
    <td align="right">0.0169</td>
    <td align="right">72.56</td>
    <td align="right">87.47</td>
    <td align="right">132.57</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
