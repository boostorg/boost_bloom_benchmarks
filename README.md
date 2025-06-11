# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for several configurations of `boost::bloom::filter<int, ...>`
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
    <td align="right">26.93</td>
    <td align="right">5.57</td>
    <td align="right">4.50</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">12.85</td>
    <td align="right">11.69</td>
    <td align="right">18.00</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.86</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.84</td>
    <td align="right">4.96</td>
    <td align="right">4.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">19.41</td>
    <td align="right">16.96</td>
    <td align="right">18.84</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.41</td>
    <td align="right">5.05</td>
    <td align="right">5.06</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.21</td>
    <td align="right">5.46</td>
    <td align="right">5.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.09</td>
    <td align="right">20.02</td>
    <td align="right">17.70</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.00</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.84</td>
    <td align="right">5.94</td>
    <td align="right">5.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">28.26</td>
    <td align="right">25.02</td>
    <td align="right">18.10</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.58</td>
    <td align="right">5.77</td>
    <td align="right">5.78</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.26</td>
    <td align="right">6.26</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">5.20</td>
    <td align="right">5.52</td>
    <td align="right">5.53</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.47</td>
    <td align="right">6.66</td>
    <td align="right">6.66</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.22</td>
    <td align="right">3.39</td>
    <td align="right">3.39</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.07</td>
    <td align="right">7.74</td>
    <td align="right">7.73</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.21</td>
    <td align="right">10.15</td>
    <td align="right">10.15</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.56</td>
    <td align="right">3.09</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.19</td>
    <td align="right">11.34</td>
    <td align="right">11.34</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">22.42</td>
    <td align="right">13.51</td>
    <td align="right">13.52</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">6.17</td>
    <td align="right">5.87</td>
    <td align="right">4.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.26</td>
    <td align="right">13.06</td>
    <td align="right">13.09</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.31</td>
    <td align="right">15.95</td>
    <td align="right">15.94</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">6.22</td>
    <td align="right">5.89</td>
    <td align="right">4.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">3.21</td>
    <td align="right">3.21</td>
    <td align="right">3.28</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.61</td>
    <td align="right">5.20</td>
    <td align="right">5.20</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.69</td>
    <td align="right">5.02</td>
    <td align="right">5.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.35</td>
    <td align="right">3.34</td>
    <td align="right">3.29</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.42</td>
    <td align="right">4.46</td>
    <td align="right">4.47</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.73</td>
    <td align="right">5.16</td>
    <td align="right">5.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.62</td>
    <td align="right">5.53</td>
    <td align="right">4.00</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.53</td>
    <td align="right">8.14</td>
    <td align="right">6.27</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.91</td>
    <td align="right">7.94</td>
    <td align="right">6.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.66</td>
    <td align="right">5.57</td>
    <td align="right">3.96</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">9.13</td>
    <td align="right">9.46</td>
    <td align="right">6.35</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.96</td>
    <td align="right">9.09</td>
    <td align="right">6.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">6.19</td>
    <td align="right">7.66</td>
    <td align="right">15.02</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.38</td>
    <td align="right">9.73</td>
    <td align="right">19.35</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.86</td>
    <td align="right">10.95</td>
    <td align="right">10.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">8.82</td>
    <td align="right">9.81</td>
    <td align="right">13.80</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.10</td>
    <td align="right">10.18</td>
    <td align="right">15.58</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.67</td>
    <td align="right">14.24</td>
    <td align="right">14.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.88</td>
    <td align="right">11.39</td>
    <td align="right">13.44</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.73</td>
    <td align="right">12.60</td>
    <td align="right">16.65</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">16.40</td>
    <td align="right">16.15</td>
    <td align="right">16.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">13.28</td>
    <td align="right">13.93</td>
    <td align="right">14.76</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.10</td>
    <td align="right">14.84</td>
    <td align="right">16.15</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">21.04</td>
    <td align="right">21.19</td>
    <td align="right">21.21</td>
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
    <td align="right">48.42</td>
    <td align="right">24.30</td>
    <td align="right">15.28</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">17.90</td>
    <td align="right">15.33</td>
    <td align="right">20.61</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">5.50</td>
    <td align="right">6.30</td>
    <td align="right">6.26</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">6.05</td>
    <td align="right">5.97</td>
    <td align="right">5.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">44.15</td>
    <td align="right">40.78</td>
    <td align="right">24.67</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">10.46</td>
    <td align="right">11.07</td>
    <td align="right">11.01</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.73</td>
    <td align="right">12.27</td>
    <td align="right">11.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">87.31</td>
    <td align="right">82.44</td>
    <td align="right">31.10</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.46</td>
    <td align="right">17.98</td>
    <td align="right">17.98</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">18.81</td>
    <td align="right">18.75</td>
    <td align="right">18.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">126.87</td>
    <td align="right">116.19</td>
    <td align="right">36.57</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">21.86</td>
    <td align="right">21.84</td>
    <td align="right">21.83</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">25.59</td>
    <td align="right">22.65</td>
    <td align="right">22.63</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">5.99</td>
    <td align="right">6.34</td>
    <td align="right">6.32</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.98</td>
    <td align="right">9.39</td>
    <td align="right">9.48</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">4.72</td>
    <td align="right">4.91</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.32</td>
    <td align="right">13.74</td>
    <td align="right">13.71</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">17.50</td>
    <td align="right">20.20</td>
    <td align="right">20.27</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">7.41</td>
    <td align="right">8.54</td>
    <td align="right">8.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">29.55</td>
    <td align="right">29.82</td>
    <td align="right">29.83</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">37.34</td>
    <td align="right">32.44</td>
    <td align="right">32.43</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">19.18</td>
    <td align="right">20.14</td>
    <td align="right">14.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">39.40</td>
    <td align="right">39.07</td>
    <td align="right">39.09</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">41.10</td>
    <td align="right">51.00</td>
    <td align="right">51.00</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">22.37</td>
    <td align="right">23.37</td>
    <td align="right">16.63</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">4.24</td>
    <td align="right">4.63</td>
    <td align="right">4.39</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">7.30</td>
    <td align="right">8.55</td>
    <td align="right">8.17</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.58</td>
    <td align="right">6.07</td>
    <td align="right">6.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">8.13</td>
    <td align="right">8.94</td>
    <td align="right">8.96</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">8.84</td>
    <td align="right">10.69</td>
    <td align="right">10.52</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">10.05</td>
    <td align="right">11.87</td>
    <td align="right">11.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">17.93</td>
    <td align="right">18.71</td>
    <td align="right">14.52</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.62</td>
    <td align="right">25.96</td>
    <td align="right">21.39</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">25.48</td>
    <td align="right">25.83</td>
    <td align="right">20.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">20.96</td>
    <td align="right">21.38</td>
    <td align="right">16.34</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">32.57</td>
    <td align="right">35.91</td>
    <td align="right">24.89</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">29.88</td>
    <td align="right">33.12</td>
    <td align="right">24.18</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">8.17</td>
    <td align="right">9.71</td>
    <td align="right">16.91</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">13.94</td>
    <td align="right">11.93</td>
    <td align="right">22.72</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">19.38</td>
    <td align="right">19.18</td>
    <td align="right">19.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">18.92</td>
    <td align="right">19.00</td>
    <td align="right">18.55</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">23.53</td>
    <td align="right">21.60</td>
    <td align="right">20.16</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">32.25</td>
    <td align="right">32.25</td>
    <td align="right">32.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">27.05</td>
    <td align="right">26.97</td>
    <td align="right">20.94</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">39.12</td>
    <td align="right">33.20</td>
    <td align="right">25.06</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">47.68</td>
    <td align="right">50.25</td>
    <td align="right">50.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">41.64</td>
    <td align="right">41.89</td>
    <td align="right">24.57</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">51.57</td>
    <td align="right">50.00</td>
    <td align="right">27.55</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.60</td>
    <td align="right">73.53</td>
    <td align="right">73.58</td>
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
    <td align="right">26.23</td>
    <td align="right">6.53</td>
    <td align="right">4.26</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">9.59</td>
    <td align="right">10.62</td>
    <td align="right">17.14</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.57</td>
    <td align="right">4.05</td>
    <td align="right">4.05</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.12</td>
    <td align="right">4.66</td>
    <td align="right">4.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">14.47</td>
    <td align="right">15.41</td>
    <td align="right">18.42</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.15</td>
    <td align="right">4.66</td>
    <td align="right">4.67</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.67</td>
    <td align="right">5.50</td>
    <td align="right">5.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.74</td>
    <td align="right">18.47</td>
    <td align="right">17.01</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.63</td>
    <td align="right">5.05</td>
    <td align="right">5.05</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.00</td>
    <td align="right">5.96</td>
    <td align="right">5.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.81</td>
    <td align="right">23.12</td>
    <td align="right">17.49</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.00</td>
    <td align="right">5.61</td>
    <td align="right">5.60</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">3.30</td>
    <td align="right">3.49</td>
    <td align="right">3.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">3.33</td>
    <td align="right">3.90</td>
    <td align="right">3.90</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.39</td>
    <td align="right">3.73</td>
    <td align="right">3.73</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.84</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.98</td>
    <td align="right">4.74</td>
    <td align="right">4.74</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.00</td>
    <td align="right">4.91</td>
    <td align="right">4.89</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.26</td>
    <td align="right">2.31</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">6.03</td>
    <td align="right">7.85</td>
    <td align="right">7.76</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">6.14</td>
    <td align="right">7.56</td>
    <td align="right">7.56</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.41</td>
    <td align="right">4.35</td>
    <td align="right">3.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.50</td>
    <td align="right">8.46</td>
    <td align="right">8.46</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">7.00</td>
    <td align="right">8.59</td>
    <td align="right">8.63</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.44</td>
    <td align="right">4.38</td>
    <td align="right">3.20</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.83</td>
    <td align="right">2.37</td>
    <td align="right">2.38</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.90</td>
    <td align="right">4.13</td>
    <td align="right">4.13</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.97</td>
    <td align="right">3.94</td>
    <td align="right">3.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.90</td>
    <td align="right">2.42</td>
    <td align="right">2.42</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.22</td>
    <td align="right">3.83</td>
    <td align="right">3.83</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.12</td>
    <td align="right">4.05</td>
    <td align="right">4.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.53</td>
    <td align="right">4.31</td>
    <td align="right">3.00</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.86</td>
    <td align="right">6.34</td>
    <td align="right">4.67</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">6.08</td>
    <td align="right">6.12</td>
    <td align="right">4.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.56</td>
    <td align="right">4.31</td>
    <td align="right">2.99</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.99</td>
    <td align="right">7.13</td>
    <td align="right">4.65</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">7.29</td>
    <td align="right">6.85</td>
    <td align="right">4.44</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">6.95</td>
    <td align="right">6.99</td>
    <td align="right">13.88</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">13.30</td>
    <td align="right">8.16</td>
    <td align="right">18.54</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.59</td>
    <td align="right">11.06</td>
    <td align="right">11.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.46</td>
    <td align="right">9.59</td>
    <td align="right">13.72</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.63</td>
    <td align="right">9.98</td>
    <td align="right">15.64</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.54</td>
    <td align="right">14.44</td>
    <td align="right">14.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.56</td>
    <td align="right">11.24</td>
    <td align="right">13.52</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">16.86</td>
    <td align="right">12.67</td>
    <td align="right">16.68</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">16.08</td>
    <td align="right">16.53</td>
    <td align="right">15.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">15.19</td>
    <td align="right">13.60</td>
    <td align="right">14.01</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">18.46</td>
    <td align="right">14.79</td>
    <td align="right">16.20</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">23.08</td>
    <td align="right">21.47</td>
    <td align="right">21.05</td>
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
    <td align="right">50.59</td>
    <td align="right">23.72</td>
    <td align="right">14.31</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">15.09</td>
    <td align="right">16.30</td>
    <td align="right">20.03</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.69</td>
    <td align="right">5.28</td>
    <td align="right">5.30</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.06</td>
    <td align="right">5.74</td>
    <td align="right">5.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">41.42</td>
    <td align="right">43.35</td>
    <td align="right">25.34</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.87</td>
    <td align="right">9.59</td>
    <td align="right">9.66</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">10.75</td>
    <td align="right">12.01</td>
    <td align="right">12.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">70.44</td>
    <td align="right">73.32</td>
    <td align="right">29.70</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.26</td>
    <td align="right">17.55</td>
    <td align="right">17.56</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.81</td>
    <td align="right">20.44</td>
    <td align="right">20.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">103.98</td>
    <td align="right">103.69</td>
    <td align="right">35.11</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.37</td>
    <td align="right">21.53</td>
    <td align="right">21.58</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">13.60</td>
    <td align="right">15.31</td>
    <td align="right">15.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">3.97</td>
    <td align="right">4.54</td>
    <td align="right">4.55</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.47</td>
    <td align="right">6.21</td>
    <td align="right">6.31</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.55</td>
    <td align="right">3.38</td>
    <td align="right">3.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.05</td>
    <td align="right">10.34</td>
    <td align="right">10.34</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.78</td>
    <td align="right">11.20</td>
    <td align="right">11.28</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">6.41</td>
    <td align="right">6.65</td>
    <td align="right">6.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">19.70</td>
    <td align="right">22.46</td>
    <td align="right">22.44</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">19.80</td>
    <td align="right">22.42</td>
    <td align="right">22.41</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">14.83</td>
    <td align="right">16.08</td>
    <td align="right">11.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">24.37</td>
    <td align="right">30.31</td>
    <td align="right">30.32</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">25.03</td>
    <td align="right">31.58</td>
    <td align="right">31.60</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">17.13</td>
    <td align="right">18.19</td>
    <td align="right">13.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">3.73</td>
    <td align="right">3.45</td>
    <td align="right">3.45</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.66</td>
    <td align="right">5.05</td>
    <td align="right">5.06</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.52</td>
    <td align="right">5.84</td>
    <td align="right">5.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">7.53</td>
    <td align="right">7.58</td>
    <td align="right">7.59</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">7.85</td>
    <td align="right">8.99</td>
    <td align="right">9.08</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">10.36</td>
    <td align="right">11.78</td>
    <td align="right">11.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">14.92</td>
    <td align="right">16.11</td>
    <td align="right">11.68</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.83</td>
    <td align="right">21.41</td>
    <td align="right">16.97</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">19.86</td>
    <td align="right">21.19</td>
    <td align="right">16.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">17.35</td>
    <td align="right">18.28</td>
    <td align="right">13.21</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">24.97</td>
    <td align="right">26.91</td>
    <td align="right">19.80</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">25.37</td>
    <td align="right">26.91</td>
    <td align="right">19.44</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">8.58</td>
    <td align="right">8.52</td>
    <td align="right">15.32</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">13.86</td>
    <td align="right">9.73</td>
    <td align="right">20.08</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">13.63</td>
    <td align="right">14.45</td>
    <td align="right">14.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">16.86</td>
    <td align="right">16.40</td>
    <td align="right">17.67</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">22.50</td>
    <td align="right">20.48</td>
    <td align="right">19.99</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">29.65</td>
    <td align="right">29.73</td>
    <td align="right">30.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">27.92</td>
    <td align="right">27.00</td>
    <td align="right">21.72</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">42.13</td>
    <td align="right">33.14</td>
    <td align="right">25.16</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">47.06</td>
    <td align="right">47.36</td>
    <td align="right">47.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">44.48</td>
    <td align="right">41.83</td>
    <td align="right">24.42</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">53.67</td>
    <td align="right">50.28</td>
    <td align="right">27.84</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">80.17</td>
    <td align="right">73.52</td>
    <td align="right">73.42</td>
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
    <td align="right">18.75</td>
    <td align="right">2.41</td>
    <td align="right">1.99</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">6.33</td>
    <td align="right">4.38</td>
    <td align="right">11.34</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.31</td>
    <td align="right">1.19</td>
    <td align="right">1.18</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.61</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">9.49</td>
    <td align="right">6.63</td>
    <td align="right">11.73</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.36</td>
    <td align="right">1.34</td>
    <td align="right">1.34</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.70</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">12.41</td>
    <td align="right">8.19</td>
    <td align="right">10.97</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.53</td>
    <td align="right">1.54</td>
    <td align="right">1.54</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.74</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">15.61</td>
    <td align="right">10.74</td>
    <td align="right">11.22</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.73</td>
    <td align="right">1.75</td>
    <td align="right">1.75</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.80</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.28</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.27</td>
    <td align="right">1.74</td>
    <td align="right">1.75</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.03</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.16</td>
    <td align="right">1.84</td>
    <td align="right">1.84</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.73</td>
    <td align="right">2.22</td>
    <td align="right">2.13</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.49</td>
    <td align="right">1.35</td>
    <td align="right">1.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.07</td>
    <td align="right">2.89</td>
    <td align="right">2.90</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.08</td>
    <td align="right">3.01</td>
    <td align="right">3.02</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">2.91</td>
    <td align="right">2.38</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.54</td>
    <td align="right">3.32</td>
    <td align="right">3.33</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.66</td>
    <td align="right">3.58</td>
    <td align="right">3.60</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">2.93</td>
    <td align="right">2.93</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.02</td>
    <td align="right">1.70</td>
    <td align="right">1.67</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.30</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.27</td>
    <td align="right">1.73</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.02</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.15</td>
    <td align="right">1.84</td>
    <td align="right">1.84</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.80</td>
    <td align="right">2.14</td>
    <td align="right">2.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">2.88</td>
    <td align="right">2.39</td>
    <td align="right">1.74</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.08</td>
    <td align="right">2.92</td>
    <td align="right">2.92</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.07</td>
    <td align="right">3.02</td>
    <td align="right">3.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">2.88</td>
    <td align="right">2.85</td>
    <td align="right">1.72</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.62</td>
    <td align="right">3.36</td>
    <td align="right">3.44</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.70</td>
    <td align="right">3.58</td>
    <td align="right">3.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">3.13</td>
    <td align="right">3.17</td>
    <td align="right">10.13</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">6.99</td>
    <td align="right">3.91</td>
    <td align="right">12.64</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">7.72</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">4.27</td>
    <td align="right">4.29</td>
    <td align="right">9.89</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">7.43</td>
    <td align="right">4.58</td>
    <td align="right">10.47</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">10.95</td>
    <td align="right">6.91</td>
    <td align="right">6.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">5.41</td>
    <td align="right">5.19</td>
    <td align="right">9.65</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">8.57</td>
    <td align="right">5.79</td>
    <td align="right">11.23</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">12.07</td>
    <td align="right">7.57</td>
    <td align="right">7.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">6.86</td>
    <td align="right">6.23</td>
    <td align="right">10.11</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">9.52</td>
    <td align="right">6.41</td>
    <td align="right">10.75</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">17.68</td>
    <td align="right">10.68</td>
    <td align="right">10.66</td>
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
    <td align="right">23.51</td>
    <td align="right">10.96</td>
    <td align="right">6.04</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">7.73</td>
    <td align="right">6.33</td>
    <td align="right">13.02</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">2.04</td>
    <td align="right">1.97</td>
    <td align="right">1.99</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.18</td>
    <td align="right">2.12</td>
    <td align="right">2.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">13.83</td>
    <td align="right">12.20</td>
    <td align="right">16.03</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">3.63</td>
    <td align="right">3.29</td>
    <td align="right">3.38</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">3.24</td>
    <td align="right">3.33</td>
    <td align="right">3.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">30.48</td>
    <td align="right">25.52</td>
    <td align="right">17.61</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.58</td>
    <td align="right">6.33</td>
    <td align="right">6.21</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.51</td>
    <td align="right">6.01</td>
    <td align="right">6.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">54.21</td>
    <td align="right">40.91</td>
    <td align="right">20.82</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.97</td>
    <td align="right">7.80</td>
    <td align="right">7.81</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.66</td>
    <td align="right">6.82</td>
    <td align="right">6.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">2.73</td>
    <td align="right">2.55</td>
    <td align="right">2.63</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.74</td>
    <td align="right">2.66</td>
    <td align="right">2.65</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.41</td>
    <td align="right">2.56</td>
    <td align="right">2.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.90</td>
    <td align="right">4.25</td>
    <td align="right">4.28</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.31</td>
    <td align="right">4.79</td>
    <td align="right">4.78</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.77</td>
    <td align="right">3.35</td>
    <td align="right">3.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.38</td>
    <td align="right">9.50</td>
    <td align="right">9.55</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">11.31</td>
    <td align="right">9.78</td>
    <td align="right">9.73</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.50</td>
    <td align="right">8.03</td>
    <td align="right">5.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.63</td>
    <td align="right">13.04</td>
    <td align="right">13.12</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">15.82</td>
    <td align="right">13.30</td>
    <td align="right">12.94</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">9.57</td>
    <td align="right">10.51</td>
    <td align="right">6.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.37</td>
    <td align="right">2.59</td>
    <td align="right">2.61</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.75</td>
    <td align="right">2.59</td>
    <td align="right">2.62</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.76</td>
    <td align="right">2.66</td>
    <td align="right">2.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.12</td>
    <td align="right">3.43</td>
    <td align="right">3.44</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">4.19</td>
    <td align="right">4.53</td>
    <td align="right">4.34</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.35</td>
    <td align="right">4.75</td>
    <td align="right">4.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.58</td>
    <td align="right">7.79</td>
    <td align="right">5.35</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.07</td>
    <td align="right">10.19</td>
    <td align="right">9.87</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">10.86</td>
    <td align="right">9.65</td>
    <td align="right">9.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.47</td>
    <td align="right">11.22</td>
    <td align="right">6.42</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.55</td>
    <td align="right">12.71</td>
    <td align="right">12.52</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.74</td>
    <td align="right">13.74</td>
    <td align="right">13.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">4.59</td>
    <td align="right">4.25</td>
    <td align="right">11.31</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">8.92</td>
    <td align="right">5.00</td>
    <td align="right">13.60</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">9.08</td>
    <td align="right">6.98</td>
    <td align="right">6.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">7.94</td>
    <td align="right">7.21</td>
    <td align="right">12.22</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.43</td>
    <td align="right">8.32</td>
    <td align="right">13.11</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">15.28</td>
    <td align="right">12.28</td>
    <td align="right">12.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">16.31</td>
    <td align="right">13.91</td>
    <td align="right">14.12</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">24.36</td>
    <td align="right">15.09</td>
    <td align="right">15.94</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">26.49</td>
    <td align="right">22.91</td>
    <td align="right">22.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">22.52</td>
    <td align="right">17.90</td>
    <td align="right">15.22</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">30.21</td>
    <td align="right">21.19</td>
    <td align="right">17.29</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">49.89</td>
    <td align="right">38.45</td>
    <td align="right">38.76</td>
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
    <td align="right">25.17</td>
    <td align="right">5.16</td>
    <td align="right">3.68</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">9.26</td>
    <td align="right">10.50</td>
    <td align="right">14.08</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.71</td>
    <td align="right">3.44</td>
    <td align="right">3.43</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.27</td>
    <td align="right">4.11</td>
    <td align="right">4.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.57</td>
    <td align="right">14.83</td>
    <td align="right">14.80</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.33</td>
    <td align="right">3.86</td>
    <td align="right">3.82</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.95</td>
    <td align="right">4.72</td>
    <td align="right">4.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.32</td>
    <td align="right">18.07</td>
    <td align="right">13.79</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.43</td>
    <td align="right">4.27</td>
    <td align="right">4.23</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.56</td>
    <td align="right">5.06</td>
    <td align="right">5.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">28.09</td>
    <td align="right">49.72</td>
    <td align="right">17.14</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">7.25</td>
    <td align="right">4.65</td>
    <td align="right">4.65</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.15</td>
    <td align="right">5.49</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">5.28</td>
    <td align="right">4.22</td>
    <td align="right">4.22</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">7.86</td>
    <td align="right">4.54</td>
    <td align="right">4.57</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.85</td>
    <td align="right">2.10</td>
    <td align="right">2.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.16</td>
    <td align="right">6.96</td>
    <td align="right">6.93</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.93</td>
    <td align="right">6.88</td>
    <td align="right">6.84</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.79</td>
    <td align="right">2.91</td>
    <td align="right">2.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.47</td>
    <td align="right">9.24</td>
    <td align="right">9.14</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">12.53</td>
    <td align="right">10.20</td>
    <td align="right">10.33</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.25</td>
    <td align="right">4.37</td>
    <td align="right">3.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.89</td>
    <td align="right">19.27</td>
    <td align="right">19.23</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">14.12</td>
    <td align="right">12.22</td>
    <td align="right">12.20</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">7.94</td>
    <td align="right">4.38</td>
    <td align="right">3.05</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">2.84</td>
    <td align="right">1.90</td>
    <td align="right">1.90</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.71</td>
    <td align="right">3.18</td>
    <td align="right">3.18</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.77</td>
    <td align="right">2.99</td>
    <td align="right">2.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.20</td>
    <td align="right">3.25</td>
    <td align="right">2.58</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.19</td>
    <td align="right">3.74</td>
    <td align="right">3.16</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">5.96</td>
    <td align="right">4.45</td>
    <td align="right">3.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.55</td>
    <td align="right">4.20</td>
    <td align="right">2.91</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.76</td>
    <td align="right">6.31</td>
    <td align="right">4.83</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.33</td>
    <td align="right">6.19</td>
    <td align="right">4.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.39</td>
    <td align="right">4.23</td>
    <td align="right">2.88</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">12.28</td>
    <td align="right">6.82</td>
    <td align="right">4.82</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.66</td>
    <td align="right">6.66</td>
    <td align="right">4.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">6.89</td>
    <td align="right">6.52</td>
    <td align="right">11.25</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">9.62</td>
    <td align="right">8.80</td>
    <td align="right">13.97</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">9.93</td>
    <td align="right">8.82</td>
    <td align="right">8.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.73</td>
    <td align="right">9.62</td>
    <td align="right">11.88</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">11.57</td>
    <td align="right">11.07</td>
    <td align="right">13.08</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">13.77</td>
    <td align="right">12.80</td>
    <td align="right">12.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.37</td>
    <td align="right">16.57</td>
    <td align="right">15.02</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">13.99</td>
    <td align="right">13.17</td>
    <td align="right">12.54</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">15.29</td>
    <td align="right">20.89</td>
    <td align="right">21.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.51</td>
    <td align="right">13.82</td>
    <td align="right">12.43</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">16.04</td>
    <td align="right">15.03</td>
    <td align="right">12.32</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">23.40</td>
    <td align="right">40.43</td>
    <td align="right">43.24</td>
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
    <td align="right">42.35</td>
    <td align="right">23.78</td>
    <td align="right">15.89</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">9.97</td>
    <td align="right">11.01</td>
    <td align="right">15.46</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.07</td>
    <td align="right">3.72</td>
    <td align="right">3.71</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.62</td>
    <td align="right">4.41</td>
    <td align="right">4.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">16.91</td>
    <td align="right">17.02</td>
    <td align="right">16.42</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.22</td>
    <td align="right">5.75</td>
    <td align="right">5.60</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">7.07</td>
    <td align="right">6.68</td>
    <td align="right">6.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">66.89</td>
    <td align="right">77.31</td>
    <td align="right">25.65</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">15.45</td>
    <td align="right">14.79</td>
    <td align="right">14.76</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.25</td>
    <td align="right">15.88</td>
    <td align="right">15.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">96.38</td>
    <td align="right">109.69</td>
    <td align="right">29.54</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.55</td>
    <td align="right">16.60</td>
    <td align="right">16.63</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">20.38</td>
    <td align="right">22.50</td>
    <td align="right">22.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">5.96</td>
    <td align="right">4.58</td>
    <td align="right">4.55</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">8.11</td>
    <td align="right">4.93</td>
    <td align="right">4.92</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.20</td>
    <td align="right">2.36</td>
    <td align="right">2.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">10.44</td>
    <td align="right">9.23</td>
    <td align="right">9.04</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.56</td>
    <td align="right">20.01</td>
    <td align="right">20.00</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">5.06</td>
    <td align="right">5.09</td>
    <td align="right">4.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">25.81</td>
    <td align="right">23.60</td>
    <td align="right">23.68</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">29.92</td>
    <td align="right">28.22</td>
    <td align="right">28.24</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">14.11</td>
    <td align="right">15.56</td>
    <td align="right">11.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">35.77</td>
    <td align="right">34.58</td>
    <td align="right">34.76</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">39.59</td>
    <td align="right">37.71</td>
    <td align="right">37.71</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">16.33</td>
    <td align="right">17.82</td>
    <td align="right">12.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">7.67</td>
    <td align="right">6.09</td>
    <td align="right">6.09</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.10</td>
    <td align="right">3.45</td>
    <td align="right">3.43</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.16</td>
    <td align="right">3.22</td>
    <td align="right">3.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">5.23</td>
    <td align="right">5.19</td>
    <td align="right">4.35</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">6.21</td>
    <td align="right">5.55</td>
    <td align="right">5.11</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">8.08</td>
    <td align="right">6.77</td>
    <td align="right">6.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">15.69</td>
    <td align="right">15.80</td>
    <td align="right">11.12</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">22.86</td>
    <td align="right">18.34</td>
    <td align="right">15.43</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">23.67</td>
    <td align="right">18.81</td>
    <td align="right">15.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">19.24</td>
    <td align="right">18.86</td>
    <td align="right">12.84</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">29.40</td>
    <td align="right">26.49</td>
    <td align="right">18.73</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">29.71</td>
    <td align="right">24.34</td>
    <td align="right">18.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">7.53</td>
    <td align="right">7.29</td>
    <td align="right">12.01</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">10.21</td>
    <td align="right">9.63</td>
    <td align="right">14.67</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">11.38</td>
    <td align="right">9.93</td>
    <td align="right">9.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">11.29</td>
    <td align="right">12.33</td>
    <td align="right">13.84</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">15.22</td>
    <td align="right">15.15</td>
    <td align="right">14.96</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">15.71</td>
    <td align="right">14.03</td>
    <td align="right">14.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">25.43</td>
    <td align="right">26.85</td>
    <td align="right">20.03</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">33.17</td>
    <td align="right">32.55</td>
    <td align="right">19.68</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">40.43</td>
    <td align="right">39.89</td>
    <td align="right">39.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">35.60</td>
    <td align="right">34.93</td>
    <td align="right">23.03</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">42.41</td>
    <td align="right">41.36</td>
    <td align="right">21.84</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">67.85</td>
    <td align="right">63.58</td>
    <td align="right">63.72</td>
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
    <td align="right">74.43</td>
    <td align="right">38.06</td>
    <td align="right">14.40</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">27.96</td>
    <td align="right">44.69</td>
    <td align="right">38.08</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">13.38</td>
    <td align="right">18.11</td>
    <td align="right">17.87</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">17.26</td>
    <td align="right">20.11</td>
    <td align="right">20.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">41.61</td>
    <td align="right">67.44</td>
    <td align="right">40.49</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">18.39</td>
    <td align="right">21.26</td>
    <td align="right">21.51</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.20</td>
    <td align="right">18.94</td>
    <td align="right">18.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">50.69</td>
    <td align="right">83.29</td>
    <td align="right">40.16</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.48</td>
    <td align="right">19.26</td>
    <td align="right">19.80</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">17.33</td>
    <td align="right">21.08</td>
    <td align="right">21.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">64.28</td>
    <td align="right">105.14</td>
    <td align="right">39.96</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.55</td>
    <td align="right">20.85</td>
    <td align="right">20.82</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.14</td>
    <td align="right">21.99</td>
    <td align="right">23.00</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">19.39</td>
    <td align="right">22.62</td>
    <td align="right">22.56</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">25.59</td>
    <td align="right">26.31</td>
    <td align="right">26.57</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">12.54</td>
    <td align="right">15.75</td>
    <td align="right">15.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">25.83</td>
    <td align="right">29.50</td>
    <td align="right">29.60</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">36.31</td>
    <td align="right">32.48</td>
    <td align="right">32.46</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">14.13</td>
    <td align="right">17.74</td>
    <td align="right">17.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">32.15</td>
    <td align="right">35.80</td>
    <td align="right">35.70</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">68.75</td>
    <td align="right">49.07</td>
    <td align="right">49.22</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">16.77</td>
    <td align="right">20.69</td>
    <td align="right">20.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.18</td>
    <td align="right">40.22</td>
    <td align="right">40.43</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">82.49</td>
    <td align="right">58.28</td>
    <td align="right">58.06</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">24.25</td>
    <td align="right">24.92</td>
    <td align="right">25.15</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">14.39</td>
    <td align="right">16.06</td>
    <td align="right">16.02</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">19.61</td>
    <td align="right">22.67</td>
    <td align="right">22.64</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">25.58</td>
    <td align="right">26.35</td>
    <td align="right">26.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.29</td>
    <td align="right">19.73</td>
    <td align="right">19.50</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">26.54</td>
    <td align="right">29.49</td>
    <td align="right">29.69</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">36.33</td>
    <td align="right">32.50</td>
    <td align="right">32.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">23.06</td>
    <td align="right">23.95</td>
    <td align="right">23.93</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">32.11</td>
    <td align="right">35.78</td>
    <td align="right">35.71</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">68.72</td>
    <td align="right">49.03</td>
    <td align="right">49.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">31.80</td>
    <td align="right">32.95</td>
    <td align="right">32.79</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.22</td>
    <td align="right">40.25</td>
    <td align="right">40.29</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">82.54</td>
    <td align="right">58.34</td>
    <td align="right">58.09</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">17.91</td>
    <td align="right">24.52</td>
    <td align="right">27.26</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">32.83</td>
    <td align="right">30.09</td>
    <td align="right">35.90</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">31.83</td>
    <td align="right">34.52</td>
    <td align="right">34.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">31.42</td>
    <td align="right">38.24</td>
    <td align="right">29.15</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">45.95</td>
    <td align="right">39.64</td>
    <td align="right">32.86</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">43.03</td>
    <td align="right">44.43</td>
    <td align="right">44.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">37.65</td>
    <td align="right">45.02</td>
    <td align="right">28.69</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">48.45</td>
    <td align="right">47.85</td>
    <td align="right">34.34</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">44.75</td>
    <td align="right">47.17</td>
    <td align="right">47.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">42.33</td>
    <td align="right">50.57</td>
    <td align="right">29.70</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">51.43</td>
    <td align="right">51.37</td>
    <td align="right">34.23</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">62.72</td>
    <td align="right">65.06</td>
    <td align="right">64.93</td>
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
    <td align="right">108.02</td>
    <td align="right">126.24</td>
    <td align="right">26.58</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">30.11</td>
    <td align="right">47.44</td>
    <td align="right">43.05</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">13.73</td>
    <td align="right">18.68</td>
    <td align="right">18.64</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">20.13</td>
    <td align="right">25.57</td>
    <td align="right">24.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">90.80</td>
    <td align="right">130.05</td>
    <td align="right">61.12</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">27.32</td>
    <td align="right">33.77</td>
    <td align="right">33.81</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">25.73</td>
    <td align="right">31.56</td>
    <td align="right">30.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">171.93</td>
    <td align="right">247.79</td>
    <td align="right">77.64</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">38.22</td>
    <td align="right">41.54</td>
    <td align="right">46.42</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">38.65</td>
    <td align="right">50.21</td>
    <td align="right">50.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">269.41</td>
    <td align="right">405.98</td>
    <td align="right">104.13</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">47.22</td>
    <td align="right">61.95</td>
    <td align="right">62.06</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">61.09</td>
    <td align="right">64.71</td>
    <td align="right">64.61</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">25.80</td>
    <td align="right">28.99</td>
    <td align="right">28.98</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.08</td>
    <td align="right">36.50</td>
    <td align="right">36.76</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">16.28</td>
    <td align="right">20.02</td>
    <td align="right">20.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">41.74</td>
    <td align="right">44.47</td>
    <td align="right">44.64</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">57.02</td>
    <td align="right">54.74</td>
    <td align="right">54.78</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">25.24</td>
    <td align="right">28.79</td>
    <td align="right">28.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">64.63</td>
    <td align="right">68.66</td>
    <td align="right">69.10</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">101.69</td>
    <td align="right">82.11</td>
    <td align="right">81.72</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">41.78</td>
    <td align="right">44.59</td>
    <td align="right">44.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.58</td>
    <td align="right">93.30</td>
    <td align="right">93.27</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">133.99</td>
    <td align="right">108.93</td>
    <td align="right">108.83</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">69.73</td>
    <td align="right">76.28</td>
    <td align="right">76.31</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">16.66</td>
    <td align="right">19.46</td>
    <td align="right">18.31</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">22.76</td>
    <td align="right">26.54</td>
    <td align="right">26.48</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">29.64</td>
    <td align="right">33.06</td>
    <td align="right">32.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">28.55</td>
    <td align="right">28.76</td>
    <td align="right">28.66</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">39.57</td>
    <td align="right">43.52</td>
    <td align="right">43.56</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">51.85</td>
    <td align="right">49.14</td>
    <td align="right">48.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">53.24</td>
    <td align="right">47.41</td>
    <td align="right">47.42</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">67.73</td>
    <td align="right">72.12</td>
    <td align="right">72.06</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">101.96</td>
    <td align="right">80.59</td>
    <td align="right">80.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">82.14</td>
    <td align="right">86.56</td>
    <td align="right">85.15</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">86.45</td>
    <td align="right">93.21</td>
    <td align="right">93.42</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">134.36</td>
    <td align="right">109.31</td>
    <td align="right">109.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">20.55</td>
    <td align="right">28.19</td>
    <td align="right">30.06</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">35.91</td>
    <td align="right">35.78</td>
    <td align="right">40.26</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">41.08</td>
    <td align="right">40.39</td>
    <td align="right">40.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">44.52</td>
    <td align="right">52.24</td>
    <td align="right">37.96</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">60.70</td>
    <td align="right">54.16</td>
    <td align="right">44.00</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">64.64</td>
    <td align="right">66.11</td>
    <td align="right">66.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">65.68</td>
    <td align="right">73.95</td>
    <td align="right">47.24</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">84.47</td>
    <td align="right">86.74</td>
    <td align="right">57.97</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">90.83</td>
    <td align="right">93.52</td>
    <td align="right">93.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">83.55</td>
    <td align="right">91.11</td>
    <td align="right">56.27</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">103.33</td>
    <td align="right">105.73</td>
    <td align="right">66.63</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">141.98</td>
    <td align="right">141.51</td>
    <td align="right">143.52</td>
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
    <td align="right">79.11</td>
    <td align="right">14.35</td>
    <td align="right">8.55</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">15.89</td>
    <td align="right">22.95</td>
    <td align="right">28.12</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.20</td>
    <td align="right">13.46</td>
    <td align="right">13.46</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">14.83</td>
    <td align="right">16.34</td>
    <td align="right">16.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">22.29</td>
    <td align="right">33.86</td>
    <td align="right">28.80</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">15.34</td>
    <td align="right">16.59</td>
    <td align="right">16.62</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">17.15</td>
    <td align="right">18.80</td>
    <td align="right">18.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">27.83</td>
    <td align="right">46.58</td>
    <td align="right">29.42</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.57</td>
    <td align="right">19.12</td>
    <td align="right">19.13</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">20.68</td>
    <td align="right">21.58</td>
    <td align="right">21.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">35.72</td>
    <td align="right">54.59</td>
    <td align="right">29.97</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">21.05</td>
    <td align="right">22.04</td>
    <td align="right">22.02</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">23.28</td>
    <td align="right">24.37</td>
    <td align="right">24.21</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">17.28</td>
    <td align="right">17.03</td>
    <td align="right">17.05</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">16.08</td>
    <td align="right">17.21</td>
    <td align="right">17.19</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.82</td>
    <td align="right">8.72</td>
    <td align="right">8.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.99</td>
    <td align="right">26.00</td>
    <td align="right">25.98</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">24.27</td>
    <td align="right">26.09</td>
    <td align="right">26.07</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.07</td>
    <td align="right">12.40</td>
    <td align="right">12.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.28</td>
    <td align="right">36.44</td>
    <td align="right">36.38</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">33.43</td>
    <td align="right">35.51</td>
    <td align="right">35.59</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.57</td>
    <td align="right">15.41</td>
    <td align="right">15.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.32</td>
    <td align="right">38.82</td>
    <td align="right">38.83</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">42.25</td>
    <td align="right">40.66</td>
    <td align="right">40.74</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">17.62</td>
    <td align="right">20.30</td>
    <td align="right">20.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">7.25</td>
    <td align="right">8.64</td>
    <td align="right">8.49</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">17.28</td>
    <td align="right">17.03</td>
    <td align="right">17.16</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">16.12</td>
    <td align="right">17.20</td>
    <td align="right">17.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">10.95</td>
    <td align="right">12.16</td>
    <td align="right">12.17</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.99</td>
    <td align="right">25.96</td>
    <td align="right">25.95</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">24.27</td>
    <td align="right">26.09</td>
    <td align="right">26.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">13.03</td>
    <td align="right">15.29</td>
    <td align="right">15.30</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.30</td>
    <td align="right">36.41</td>
    <td align="right">36.43</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">33.38</td>
    <td align="right">35.60</td>
    <td align="right">35.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">17.54</td>
    <td align="right">19.07</td>
    <td align="right">19.08</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.34</td>
    <td align="right">38.83</td>
    <td align="right">38.82</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">42.35</td>
    <td align="right">40.70</td>
    <td align="right">40.78</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">17.09</td>
    <td align="right">18.16</td>
    <td align="right">22.51</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">47.06</td>
    <td align="right">40.79</td>
    <td align="right">40.77</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">26.11</td>
    <td align="right">27.38</td>
    <td align="right">28.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">26.63</td>
    <td align="right">27.58</td>
    <td align="right">23.32</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">51.51</td>
    <td align="right">45.68</td>
    <td align="right">38.85</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">36.64</td>
    <td align="right">35.47</td>
    <td align="right">35.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.26</td>
    <td align="right">34.69</td>
    <td align="right">23.31</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">59.27</td>
    <td align="right">53.37</td>
    <td align="right">40.26</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">39.16</td>
    <td align="right">38.01</td>
    <td align="right">37.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">38.45</td>
    <td align="right">45.38</td>
    <td align="right">28.08</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">62.76</td>
    <td align="right">57.35</td>
    <td align="right">42.17</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">51.27</td>
    <td align="right">49.67</td>
    <td align="right">49.63</td>
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
    <td align="right">123.96</td>
    <td align="right">61.85</td>
    <td align="right">23.04</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">23.10</td>
    <td align="right">32.62</td>
    <td align="right">32.79</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">14.84</td>
    <td align="right">16.33</td>
    <td align="right">16.32</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">17.51</td>
    <td align="right">18.67</td>
    <td align="right">18.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">56.03</td>
    <td align="right">74.83</td>
    <td align="right">41.32</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">26.40</td>
    <td align="right">27.92</td>
    <td align="right">27.90</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">26.97</td>
    <td align="right">30.89</td>
    <td align="right">30.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">113.47</td>
    <td align="right">163.24</td>
    <td align="right">58.03</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">39.03</td>
    <td align="right">47.52</td>
    <td align="right">47.38</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">48.60</td>
    <td align="right">49.88</td>
    <td align="right">49.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">165.36</td>
    <td align="right">239.18</td>
    <td align="right">71.63</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">62.89</td>
    <td align="right">62.09</td>
    <td align="right">62.05</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">66.54</td>
    <td align="right">65.52</td>
    <td align="right">65.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">20.28</td>
    <td align="right">20.10</td>
    <td align="right">19.89</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">19.84</td>
    <td align="right">21.24</td>
    <td align="right">21.32</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">10.21</td>
    <td align="right">11.25</td>
    <td align="right">11.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">34.40</td>
    <td align="right">40.42</td>
    <td align="right">40.33</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.96</td>
    <td align="right">43.10</td>
    <td align="right">43.06</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">19.77</td>
    <td align="right">20.84</td>
    <td align="right">20.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">69.19</td>
    <td align="right">70.53</td>
    <td align="right">70.52</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">69.35</td>
    <td align="right">71.03</td>
    <td align="right">71.08</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">37.95</td>
    <td align="right">39.16</td>
    <td align="right">40.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.70</td>
    <td align="right">86.91</td>
    <td align="right">87.15</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">94.08</td>
    <td align="right">91.09</td>
    <td align="right">91.22</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">51.92</td>
    <td align="right">52.71</td>
    <td align="right">52.61</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">9.57</td>
    <td align="right">11.07</td>
    <td align="right">11.12</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">20.16</td>
    <td align="right">20.05</td>
    <td align="right">20.25</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">19.36</td>
    <td align="right">20.76</td>
    <td align="right">20.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">21.08</td>
    <td align="right">23.06</td>
    <td align="right">21.66</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">35.28</td>
    <td align="right">40.69</td>
    <td align="right">40.73</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">39.52</td>
    <td align="right">42.21</td>
    <td align="right">42.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">36.75</td>
    <td align="right">39.24</td>
    <td align="right">39.34</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">68.79</td>
    <td align="right">68.31</td>
    <td align="right">68.29</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">68.13</td>
    <td align="right">68.00</td>
    <td align="right">68.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">51.79</td>
    <td align="right">52.82</td>
    <td align="right">52.76</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.95</td>
    <td align="right">87.06</td>
    <td align="right">87.09</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">94.35</td>
    <td align="right">93.51</td>
    <td align="right">93.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">20.30</td>
    <td align="right">21.36</td>
    <td align="right">24.85</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">49.13</td>
    <td align="right">42.52</td>
    <td align="right">43.03</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">34.48</td>
    <td align="right">37.30</td>
    <td align="right">35.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">40.97</td>
    <td align="right">38.85</td>
    <td align="right">29.52</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">66.39</td>
    <td align="right">59.02</td>
    <td align="right">49.34</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">59.25</td>
    <td align="right">56.79</td>
    <td align="right">56.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">62.37</td>
    <td align="right">63.12</td>
    <td align="right">38.87</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">91.66</td>
    <td align="right">86.92</td>
    <td align="right">63.38</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">88.36</td>
    <td align="right">82.09</td>
    <td align="right">81.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">80.74</td>
    <td align="right">86.42</td>
    <td align="right">54.09</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">108.60</td>
    <td align="right">104.77</td>
    <td align="right">73.29</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">130.58</td>
    <td align="right">117.37</td>
    <td align="right">117.36</td>
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
    <td align="right">31.82</td>
    <td align="right">6.67</td>
    <td align="right">5.67</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">50.53</td>
    <td align="right">45.57</td>
    <td align="right">32.42</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.25</td>
    <td align="right">20.10</td>
    <td align="right">21.64</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">21.96</td>
    <td align="right">24.24</td>
    <td align="right">25.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">77.19</td>
    <td align="right">66.01</td>
    <td align="right">34.77</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">19.69</td>
    <td align="right">20.24</td>
    <td align="right">21.58</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">25.12</td>
    <td align="right">25.35</td>
    <td align="right">26.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">94.33</td>
    <td align="right">79.90</td>
    <td align="right">33.37</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">23.16</td>
    <td align="right">23.04</td>
    <td align="right">24.30</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">27.36</td>
    <td align="right">27.12</td>
    <td align="right">28.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">122.07</td>
    <td align="right">101.03</td>
    <td align="right">33.49</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">24.27</td>
    <td align="right">24.49</td>
    <td align="right">25.24</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">28.87</td>
    <td align="right">29.58</td>
    <td align="right">30.02</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">21.09</td>
    <td align="right">38.26</td>
    <td align="right">38.39</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">23.53</td>
    <td align="right">38.08</td>
    <td align="right">38.57</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">16.04</td>
    <td align="right">27.61</td>
    <td align="right">27.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">25.88</td>
    <td align="right">52.47</td>
    <td align="right">52.45</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">29.99</td>
    <td align="right">52.81</td>
    <td align="right">52.62</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">15.50</td>
    <td align="right">37.19</td>
    <td align="right">27.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">35.62</td>
    <td align="right">72.67</td>
    <td align="right">73.49</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">40.59</td>
    <td align="right">72.23</td>
    <td align="right">72.99</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">25.54</td>
    <td align="right">53.74</td>
    <td align="right">36.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">39.57</td>
    <td align="right">81.79</td>
    <td align="right">82.80</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">46.01</td>
    <td align="right">85.83</td>
    <td align="right">88.61</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">25.71</td>
    <td align="right">54.21</td>
    <td align="right">37.25</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">16.52</td>
    <td align="right">27.47</td>
    <td align="right">27.45</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">18.52</td>
    <td align="right">29.64</td>
    <td align="right">29.64</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">19.21</td>
    <td align="right">29.56</td>
    <td align="right">29.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">16.55</td>
    <td align="right">43.81</td>
    <td align="right">34.28</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">17.42</td>
    <td align="right">38.33</td>
    <td align="right">28.81</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">19.01</td>
    <td align="right">46.66</td>
    <td align="right">37.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">26.17</td>
    <td align="right">53.80</td>
    <td align="right">36.43</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">29.99</td>
    <td align="right">57.64</td>
    <td align="right">39.58</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">30.89</td>
    <td align="right">57.34</td>
    <td align="right">39.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">26.00</td>
    <td align="right">54.09</td>
    <td align="right">36.90</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">31.16</td>
    <td align="right">59.41</td>
    <td align="right">39.91</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">31.99</td>
    <td align="right">59.13</td>
    <td align="right">39.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">24.62</td>
    <td align="right">41.58</td>
    <td align="right">30.77</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">30.58</td>
    <td align="right">51.46</td>
    <td align="right">33.74</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">34.61</td>
    <td align="right">58.01</td>
    <td align="right">58.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">33.15</td>
    <td align="right">57.41</td>
    <td align="right">30.80</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">37.83</td>
    <td align="right">58.14</td>
    <td align="right">31.86</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">42.81</td>
    <td align="right">75.34</td>
    <td align="right">77.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">38.29</td>
    <td align="right">70.84</td>
    <td align="right">30.85</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">45.22</td>
    <td align="right">76.71</td>
    <td align="right">33.20</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">45.81</td>
    <td align="right">82.77</td>
    <td align="right">84.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">50.53</td>
    <td align="right">96.72</td>
    <td align="right">31.81</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">54.56</td>
    <td align="right">95.82</td>
    <td align="right">32.92</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">61.61</td>
    <td align="right">113.36</td>
    <td align="right">112.80</td>
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
    <td align="right">61.43</td>
    <td align="right">33.34</td>
    <td align="right">17.12</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
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
    <td align="right">57.13</td>
    <td align="right">48.47</td>
    <td align="right">35.60</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">18.51</td>
    <td align="right">20.33</td>
    <td align="right">22.14</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">24.51</td>
    <td align="right">28.73</td>
    <td align="right">30.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">104.49</td>
    <td align="right">113.07</td>
    <td align="right">48.22</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">22.29</td>
    <td align="right">24.70</td>
    <td align="right">26.84</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">30.33</td>
    <td align="right">28.78</td>
    <td align="right">30.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">222.31</td>
    <td align="right">191.22</td>
    <td align="right">59.13</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">35.68</td>
    <td align="right">35.47</td>
    <td align="right">37.06</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">47.20</td>
    <td align="right">47.49</td>
    <td align="right">49.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">351.17</td>
    <td align="right">295.42</td>
    <td align="right">73.14</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">42.70</td>
    <td align="right">42.91</td>
    <td align="right">44.14</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">59.22</td>
    <td align="right">58.78</td>
    <td align="right">60.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
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
    <td align="right">24.44</td>
    <td align="right">38.56</td>
    <td align="right">39.17</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">26.46</td>
    <td align="right">38.39</td>
    <td align="right">38.80</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">16.37</td>
    <td align="right">29.54</td>
    <td align="right">29.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">32.43</td>
    <td align="right">54.42</td>
    <td align="right">54.58</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">37.45</td>
    <td align="right">57.36</td>
    <td align="right">56.32</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">18.92</td>
    <td align="right">41.18</td>
    <td align="right">30.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">56.57</td>
    <td align="right">87.38</td>
    <td align="right">88.21</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">63.68</td>
    <td align="right">88.78</td>
    <td align="right">89.15</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">46.71</td>
    <td align="right">79.32</td>
    <td align="right">61.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">73.78</td>
    <td align="right">105.21</td>
    <td align="right">106.08</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">84.06</td>
    <td align="right">115.97</td>
    <td align="right">117.74</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">58.29</td>
    <td align="right">92.41</td>
    <td align="right">74.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
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
    <td align="right">16.79</td>
    <td align="right">29.09</td>
    <td align="right">29.07</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">18.79</td>
    <td align="right">31.49</td>
    <td align="right">31.45</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">19.66</td>
    <td align="right">36.65</td>
    <td align="right">36.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">19.63</td>
    <td align="right">49.42</td>
    <td align="right">39.99</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">19.59</td>
    <td align="right">41.59</td>
    <td align="right">32.58</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">24.13</td>
    <td align="right">53.04</td>
    <td align="right">43.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">48.31</td>
    <td align="right">78.57</td>
    <td align="right">62.42</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">52.19</td>
    <td align="right">82.02</td>
    <td align="right">64.01</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">53.24</td>
    <td align="right">82.71</td>
    <td align="right">64.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">59.46</td>
    <td align="right">91.39</td>
    <td align="right">75.79</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">61.15</td>
    <td align="right">96.86</td>
    <td align="right">77.98</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">63.33</td>
    <td align="right">98.03</td>
    <td align="right">78.38</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">32.74</td>
    <td align="right">48.09</td>
    <td align="right">39.23</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">34.20</td>
    <td align="right">52.12</td>
    <td align="right">36.30</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">36.79</td>
    <td align="right">58.39</td>
    <td align="right">58.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">39.13</td>
    <td align="right">59.87</td>
    <td align="right">34.49</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">46.37</td>
    <td align="right">67.59</td>
    <td align="right">43.43</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">50.06</td>
    <td align="right">83.98</td>
    <td align="right">86.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">57.01</td>
    <td align="right">84.05</td>
    <td align="right">46.11</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">72.61</td>
    <td align="right">100.23</td>
    <td align="right">60.63</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">75.89</td>
    <td align="right">103.59</td>
    <td align="right">104.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">80.45</td>
    <td align="right">118.76</td>
    <td align="right">54.36</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">93.86</td>
    <td align="right">129.54</td>
    <td align="right">70.91</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">107.14</td>
    <td align="right">141.02</td>
    <td align="right">140.99</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
